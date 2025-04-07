from rest_framework import serializers

from ...models import BookModel


class BaseBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...


class RetrieveBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...


class CreateBookSerializer(BaseBookSerializer):
    class Meta(BaseBookSerializer.Meta): ...
