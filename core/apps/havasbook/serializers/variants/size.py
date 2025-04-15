from rest_framework import serializers

from ...models import SizeModel


class BaseSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListSizeSerializer(BaseSizeSerializer):
    class Meta(BaseSizeSerializer.Meta): ...


class RetrieveSizeSerializer(BaseSizeSerializer):
    class Meta(BaseSizeSerializer.Meta): ...


class CreateSizeSerializer(BaseSizeSerializer):
    class Meta(BaseSizeSerializer.Meta): ...
