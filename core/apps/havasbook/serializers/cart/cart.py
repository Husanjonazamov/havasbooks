from rest_framework import serializers
from core.apps.havasbook.serializers.cart.cartItem import CreateCartitemSerializer
from ...models import CartModel, CartitemModel
from decimal import Decimal
from django.db.models import Sum






class BaseCartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = CartModel
        fields = [
            'id',
            'user',
            'total_price'
        ]
        
    def get_user(self, obj):
        from core.apps.accounts.serializers import UserSerializer
        return UserSerializer(obj.user).data


    def to_representation(self, instance):
        rep = super().to_representation(instance)

        for field in ["total_price"]:
            value = rep.get(field)
            if value is not None:
                value = Decimal(value).quantize(Decimal('0')) 
                rep[field] = int(value) 

        return rep


class ListCartSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    total_discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = CartModel
        fields = [
            'total_price',
            'total_quantity',
            'total_discounted_price',
            'products'
        ]

    def get_products(self, obj):
        from core.apps.havasbook.serializers.cart import ListCartitemSerializer
        items = obj.cart_items.all()  # CartModeldagi related_name qiymatini "cart_item" deb qabul qilamiz
        return ListCartitemSerializer(items, many=True).data

    def get_total_quantity(self, obj):
        return sum([item.quantity for item in obj.cart_items.all()])

    def get_total_price(self, obj):
        return str(sum([item.book.price * item.quantity for item in obj.cart_items.all()]))

    def get_total_discounted_price(self, obj):
        total = 0
        for item in obj.cart_items.all():
            if hasattr(item.book, 'get_discounted_price'):
                total += item.book.get_discounted_price() * item.quantity
            else:
                total += item.book.price * item.quantity
        return total







class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...





class CreateCartSerializer(BaseCartSerializer):
    cart_items = CreateCartitemSerializer(many=True, required=True)

    class Meta(BaseCartSerializer.Meta):
        model = CartModel
        fields = BaseCartSerializer.Meta.fields + ['cart_items']

    def validate_cart_items(self, value):
        if not value:
            raise serializers.ValidationError("Cart items bo'sh bo'lishi mumkin emas.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user

        if not user or user.is_anonymous:
            raise serializers.ValidationError("Foydalanuvchi aniqlanmadi.")

        cart_items_data = validated_data.pop('cart_items')

        cart, created = CartModel.objects.get_or_create(user=user)

        total_price_sum = Decimal('0.00') 

        for item_data in cart_items_data:
            book = item_data.get('book')
            color = item_data.get('color')  
            size = item_data.get('size')   
            quantity = 1  # Default quantity

            if not book:
                raise serializers.ValidationError("Item uchun book kiritilishi kerak.")

            total_price = Decimal(book.price) * Decimal(quantity)  
            total_price_sum += total_price

            # Tekshiruv: agar bunday mahsulot allaqachon mavjud bo'lsa, quantity-ni oshiramiz
            existing_item = CartitemModel.objects.filter(
                cart=cart,
                book=book,
                color=color,
                size=size
            ).first()

            if existing_item:
                # Agar mahsulot mavjud bo'lsa, faqat quantity ni oshiramiz
                existing_item.quantity += 1
                existing_item.total_price = existing_item.book.price * existing_item.quantity
                existing_item.save()
            else:
                # Yangi item yaratish
                CartitemModel.objects.create(
                    cart=cart,
                    book=book,
                    color=color,  
                    size=size,    
                    quantity=quantity,  
                    total_price=total_price,
                )

        # Savatdagi umumiy narxni yangilash
        cart.total_price = Decimal(cart.total_price) + total_price_sum
        cart.save()

        return cart
