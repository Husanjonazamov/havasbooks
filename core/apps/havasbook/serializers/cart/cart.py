from rest_framework import serializers
from core.apps.havasbook.serializers.cart.cartItem import ListCartitemSerializer
from ...models import CartModel


class BaseCartSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = CartModel
        fields = [
            'id',
            'user',
        ]
        
    def get_user(self, obj):
        from core.apps.accounts.serializers import UserSerializer
        return UserSerializer(obj.user).data


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
