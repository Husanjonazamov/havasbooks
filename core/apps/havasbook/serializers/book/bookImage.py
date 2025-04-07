from rest_framework import serializers

from ...models import BookimageModel


class BaseBookimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookimageModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListBookimageSerializer(BaseBookimageSerializer):
    class Meta(BaseBookimageSerializer.Meta): ...


class RetrieveBookimageSerializer(BaseBookimageSerializer):
    class Meta(BaseBookimageSerializer.Meta): ...


class CreateBookimageSerializer(BaseBookimageSerializer):
    class Meta(BaseBookimageSerializer.Meta): ...
