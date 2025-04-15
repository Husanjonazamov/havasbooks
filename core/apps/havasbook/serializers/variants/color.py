from rest_framework import serializers

from ...models import ColorModel


class BaseColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...


class RetrieveColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...


class CreateColorSerializer(BaseColorSerializer):
    class Meta(BaseColorSerializer.Meta): ...
