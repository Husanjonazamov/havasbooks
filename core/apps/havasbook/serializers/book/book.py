from rest_framework import serializers
from ...models import BookModel
from decimal import Decimal


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
            'is_preorder',
            'created_at',
        ]
        
    # def get_category(self, obj):
    #     from core.apps.havasbook.serializers.category import ListCategorySerializer
        
    #     return ListCategorySerializer(obj.category).data
    
    
    def get_color(self, obj):
        from core.apps.havasbook.serializers import ListColorSerializer

        return ListColorSerializer(obj.color, many=True).data

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
    
    class Meta(BaseBookSerializer.Meta): 
        fields = [
            'id',
            'category',
            'name',
            'description',
            'original_price',
            'discount_percent',
            'price',
            'quantity',
            'is_discount',
            'images'
        ]
        
    def get_images(self, obj):
        from core.apps.havasbook.serializers.book import ListBookimageSerializer
        images = obj.images.all()
        
        return ListBookimageSerializer(images, many=True).data
        

class CreateBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...
