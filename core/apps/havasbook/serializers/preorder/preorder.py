from rest_framework import serializers

from ...models import PreorderModel


class BasePreorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreorderModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListPreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...


class RetrievePreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...


class CreatePreorderSerializer(BasePreorderSerializer):
    class Meta(BasePreorderSerializer.Meta): ...
