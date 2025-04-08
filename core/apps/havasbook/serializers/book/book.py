from rest_framework import serializers
from ...models import BookModel


class BaseBookSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = BookModel
        fields = [
            'id',
            'category',
            'name',
            'image',
            'original_price',
            'discount_percent',
            'price',
            'quantity',
            'is_discount',
        ]
        
    def get_category(self, obj):
        from core.apps.havasbook.serializers.category import ListCategorySerializer
        
        return ListCategorySerializer(obj.category).data


class ListBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...


class RetrieveBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...


class CreateBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...
