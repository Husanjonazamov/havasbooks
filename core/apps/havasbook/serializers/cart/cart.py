from rest_framework import serializers
from core.apps.havasbook.serializers.cart.cartItem import ListCartitemSerializer
from ...models import CartModel
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
        child=ListCartitemSerializer(),
        required=True
    )
    class Meta(BaseCartSerializer.Meta): ...
