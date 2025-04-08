from rest_framework import serializers
from core.apps.havasbook.serializers.cart.cartItem import CreateCartitemSerializer
from ...models import CartModel, CartitemModel
from decimal import Decimal






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


class ListCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...





class CreateCartSerializer(BaseCartSerializer):
    cart_items = serializers.ListField(
        child=CreateCartitemSerializer(),
        required=True
    )

    class Meta(BaseCartSerializer.Meta):
        model = CartModel
        fields = BaseCartSerializer.Meta.fields + ['cart_items']

    def create(self, validated_data):
        # Foydalanuvchi ma'lumotlarini olish
        user = self.context['request'].user
        
        if not user:
            raise ValueError("Request object not found in serializer context.")
        
        # 'cart_items'ni olish
        cart_items_data = validated_data.pop('cart_items', [])

        # Cart yaratish yoki mavjud bo'lsa olish
        cart = validated_data.get('cart', None)
        if not cart:
            cart, created = CartModel.objects.get_or_create(user=user)

        # Har bir cart_item uchun yaratish va narxni hisoblash
        for item_data in cart_items_data:
            item_data['cart'] = cart  # cartni bog'lash
            # Quantity va total_price ni hisoblash
            book = item_data.get('book')
            quantity = item_data.get('quantity', 1)  # agar quantity yo'q bo'lsa, 1 deb olish

            total_price = book.price * quantity  # Jami narxni hisoblash
            item_data['total_price'] = total_price  # total_price ni o'rnatish

            # CartitemModel yaratish
            CartitemModel.objects.create(**item_data)

        # Cart total_price ni yangilash
        cart.update_total_price()

        return cart


