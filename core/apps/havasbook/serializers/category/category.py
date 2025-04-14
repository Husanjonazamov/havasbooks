from rest_framework import serializers

from ...models import CategoryModel
from core.apps.havasbook.serializers.book.book import BaseBookSerializer

class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            'id',
            'name',
            'image',
        ]


class ListCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class RetrieveCategorySerializer(BaseCategorySerializer):
    books = BaseBookSerializer(many=True, read_only=True)
    class Meta(BaseCategorySerializer.Meta): 
        fields = BaseCategorySerializer.Meta.fields + ['books']


class CreateCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...
