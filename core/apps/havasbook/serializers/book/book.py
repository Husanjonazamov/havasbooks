from rest_framework import serializers
from ...models import BookModel
from decimal import Decimal

from django.conf import settings
from core.apps.havasbook.models.cart import CartitemModel, CartModel
from django_core.serializers import AbstractTranslatedSerializer



class BaseBookSerializer(AbstractTranslatedSerializer):
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    class Meta:
        model = BookModel
        translated_fields = [
            "name",
            "description"
        ]
        fields = [
            'id',
            'category',
            'name',
            'image',
            'color',
            'size',
            'original_price',
            'discount_percent',
            'price',
            'quantity',
            "book_id",
            'sold_count',
            'view_count',
            'is_discount',
            'popular',
            'is_preorder',
            'product_type',
            'created_at',
        ]
        
    # def get_category(self, obj):
    #     from core.apps.havasbook.serializers.category import ListCategorySerializer
        
    #     return ListCategorySerializer(obj.category).data
    
    
    
    
    def get_color(self, obj):
        from core.apps.havasbook.serializers.variants import BaseColorSerializer
        request = self.context.get('request')
        return BaseColorSerializer(obj.color.all(), many=True, context={'request': request}).data

    def get_size(self, obj):
        from core.apps.havasbook.serializers import ListSizeSerializer

        return ListSizeSerializer(obj.size, many=True).data


    def to_representation(self, instance):
        rep = super().to_representation(instance)

        for field in ["original_price", "discount_percent", "price"]:
            value = rep.get(field)
            if value is not None:
                value = Decimal(value)
                rep[field] = int(value) if value == int(value) else float(value)

        return rep


class ListBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...



class RetrieveBookSerializer(BaseBookSerializer):
    images = serializers.SerializerMethodField()
    cart_id = serializers.SerializerMethodField()

    class Meta(BaseBookSerializer.Meta): 
        fields = [
            'id',
            'cart_id',
            'category',
            'name',
            'description',
            'image',
            'color',
            'size',
            'original_price',
            'discount_percent',
            'price',
            'quantity',
            "book_id",
            'sold_count',
            'view_count',
            'popular',
            'is_preorder',
            'is_discount',
            'images',
            'product_type',
            'created_at',
        ]
        
    def get_images(self, obj):
        from core.apps.havasbook.serializers.book.bookImage import BaseBookimageSerializer
        request = self.context.get('request')

        images_qs = obj.book_images.all()
        images = BaseBookimageSerializer(images_qs, many=True, context={'request': request}).data
        return images



    
    def get_cart_id(self, obj):
        request = self.context.get('request')
        
        cart = CartModel.objects.filter(user=request.user).first()
        if cart:
            cart_item = CartitemModel.objects.filter(cart=cart, book=obj).first()
            
            print("Cart Item:", cart_item)
            
            if cart_item:
                return cart.id  
            else:
                print("Cart Item topilmadi!")
        else:
            print("Cart topilmadi!")

    
    # def get_images(self, obj):
    #     from core.apps.havasbook.serializers.book import ListBookimageSerializer
    #     image_instance = obj.images.first()
    #     if image_instance:
    #         return ListBookimageSerializer(image_instance, context=self.context).data
    #     return None

        

class CreateBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...
