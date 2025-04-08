from rest_framework import serializers

from ...models import CartitemModel


class BaseCartitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartitemModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class RetrieveCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class CreateCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...
