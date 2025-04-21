from rest_framework import serializers
from ...models import BookModel
from decimal import Decimal


from django.conf import settings


class BaseBookSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()
    size = serializers.SerializerMethodField()

    class Meta:
        model = BookModel
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
            'sold_count',
            'view_count',
            'is_discount',
            'popular',
            'is_preorder',
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
    # images = serializers.SerializerMethodField()
    
    class Meta(BaseBookSerializer.Meta): 
        fields = [
            'id',
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
            'sold_count',
            'view_count',
            'popular',
            'is_preorder',
            'is_discount',
            'images',
            'created_at',
        ]
        
    # def get_images(self, obj):
    #     from core.apps.havasbook.serializers.book import ListBookimageSerializer
    #     image_instance = obj.images.first()
    #     if image_instance:
    #         return ListBookimageSerializer(image_instance, context=self.context).data
    #     return None

        

class CreateBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...
