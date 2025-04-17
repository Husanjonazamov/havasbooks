from rest_framework import serializers

from ...models import CartitemModel, CartModel
from core.apps.havasbook.models.book import BookModel
from core.apps.havasbook.models.variants import ColorModel, SizeModel


class BaseCartitemSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField() 
    cart = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    
    
    class Meta:
        model = CartitemModel
        fields = [
            'id',
            'cart',
            'book',
            'color',
            'size',
            'quantity',
            'total_price'
        ]

    def get_cart(self, obj):
        from core.apps.havasbook.serializers.cart.cart import ListCartSerializer
        return ListCartSerializer(obj.cart).data  # Cartni get qilish

    def get_book(self, obj):
        from core.apps.havasbook.serializers.book import ListBookSerializer
        return ListBookSerializer(obj.book).data  # Bookni get qilish


    def get_color(self, obj):
        if obj.color:
            from core.apps.havasbook.serializers.variants import ListColorSerializer
            return ListColorSerializer(obj.color).data
        return None

    def get_size(self, obj):
        if obj.size:
            from core.apps.havasbook.serializers.variants import ListSizeSerializer
            return ListSizeSerializer(obj.size).data
        return None



class ListCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class RetrieveCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...




class CreateCartitemSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=BookModel.objects.all())
    color = serializers.PrimaryKeyRelatedField(queryset=ColorModel.objects.all(), required=False, allow_null=True)
    size = serializers.PrimaryKeyRelatedField(queryset=SizeModel.objects.all(), required=False, allow_null=True)
    quantity = serializers.IntegerField(min_value=1, default=1)
    
    class Meta:
        model = CartitemModel
        fields = [
            'id',
            'book',
            'color',
            'size',
            'quantity',
            'total_price'
        ]

    def validate(self, attrs):
        book = attrs.get('book')
        quantity = attrs.get('quantity')

        total_price = book.price * quantity

        attrs['total_price'] = total_price
        return attrs

