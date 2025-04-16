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


from decimal import Decimal

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

        total_price_sum = Decimal('0.00')  # Start with a Decimal

        for item_data in cart_items_data:
            book = item_data.get('book')
            quantity = item_data.get('quantity', 1)

            if not book:
                raise serializers.ValidationError("Item uchun book kiritilishi kerak.")

            total_price = Decimal(book.price) * Decimal(quantity)  
            total_price_sum += total_price

            CartitemModel.objects.create(
                cart=cart,
                book=book,
                quantity=quantity,
                total_price=total_price,
            )

        cart.total_price = Decimal(cart.total_price) + total_price_sum
        cart.save()

        return cart
