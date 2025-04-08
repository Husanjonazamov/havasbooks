from rest_framework import serializers

from ...models import CartitemModel, CartModel
from core.apps.havasbook.models.book import BookModel



class BaseCartitemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=BookModel.objects.all())  # Bookni olish (ID orqali)
    cart = serializers.SerializerMethodField()  # Cartni olish
    
    class Meta:
        model = CartitemModel
        fields = [
            'id',
            'cart',
            'book',
            'quantity',
            'total_price'
        ]

    def get_cart(self, obj):
        from core.apps.havasbook.serializers.cart.cart import ListCartSerializer
        return ListCartSerializer(obj.cart).data  # Cartni get qilish

    def get_book(self, obj):
        from core.apps.havasbook.serializers.book import ListBookSerializer
        return ListBookSerializer(obj.book).data  # Bookni get qilish



class ListCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class RetrieveCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class CreateCartitemSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(
        queryset=CartModel.objects.all(), 
        required=False, 
        allow_null=True
    )
    class Meta:
        model = CartitemModel
        fields = [
            'id',
            'cart',
            'book',
            'quantity',
            'total_price'
        ]