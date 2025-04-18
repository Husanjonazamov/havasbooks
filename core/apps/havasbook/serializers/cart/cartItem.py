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





class ListCartitemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='book.name')
    color = serializers.CharField(source='color.name', default=None)
    image = serializers.SerializerMethodField()
    price = serializers.DecimalField(source='book.price', max_digits=10, decimal_places=2)
    discounted_total_price = serializers.SerializerMethodField()
    discount_percent = serializers.SerializerMethodField()

    class Meta:
        model = CartitemModel
        fields = [
            'id',
            'name',
            'color',
            'image',
            'price',
            'total_price',
            'discounted_total_price',
            'quantity',
            'discount_percent',
        ]


    def get_image(self, obj):
        request = self.context.get('request')
        
        if obj.book.image and request:
            return request.build_absolute_uri(obj.book.image.url)
        return None

    def get_discounted_total_price(self, obj):
        total_price = obj.total_price or 0
        discount = getattr(obj.book, 'discount_percent', None)

        if discount is None:
            return total_price  # chegirma yo'q

        return round(total_price * (1 - discount / 100), 2)


    def get_discount_percent(self, obj):
        return getattr(obj.book, 'discount_percent', 0)


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

