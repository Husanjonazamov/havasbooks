from rest_framework import serializers
from core.apps.havasbook.serializers.cart.cartItem import ListCartitemSerializer
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
    items = serializers.ListField(
        child=ListCartitemSerializer(),
        required=True
    )

    class Meta(BaseCartSerializer.Meta):
        model = CartModel
        fields = BaseCartSerializer.Meta.fields + ['items']

    def create(self, validated_data):
        user = self.context['request'].user
        
        if not user:
            raise ValueError("Request object not found in serializer context.")
        
        # 'items' ni olish
        items_data = validated_data.pop('items')

        # Cart yaratish
        cart = CartModel.objects.create(user=user, **validated_data)

        for item_data in items_data:
            book = item_data['book']
            quantity = item_data['quantity']
            total_price = book.price * quantity

            # Cartitem yaratish
            CartitemModel.objects.create(
                cart=cart,
                book=book,
                quantity=quantity,
                total_price=total_price
            )

        cart.update_total_price()
        return cart


