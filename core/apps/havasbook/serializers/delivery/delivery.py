from rest_framework import serializers

from ...models import DeliveryModel


class BaseDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryModel
        fields = [
            'id',
            'title'
        ]


class ListDeliverySerializer(BaseDeliverySerializer):
    class Meta(BaseDeliverySerializer.Meta): ...


class RetrieveDeliverySerializer(BaseDeliverySerializer):
    class Meta(BaseDeliverySerializer.Meta): ...


class CreateDeliverySerializer(BaseDeliverySerializer):
    class Meta(BaseDeliverySerializer.Meta): ...
