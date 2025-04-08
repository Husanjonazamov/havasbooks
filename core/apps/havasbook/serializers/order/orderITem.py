from rest_framework import serializers

from ...models import OrderitemModel


class BaseOrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderitemModel
        exclude = [
            "created_at",
            "updated_at",
        ]


class ListOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class RetrieveOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class CreateOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...
