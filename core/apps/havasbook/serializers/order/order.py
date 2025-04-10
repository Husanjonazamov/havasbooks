from rest_framework import serializers

from ...models import OrderModel
from core.apps.havasbook.serializers.order.orderITem import CreateOrderitemSerializer


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = [
            'id',
            'user',
            'location',
            'delivery_method',
            'payment_method',
            'total_amount',
            'status',
            'comment'
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    order_item = serializers.CharField(
        child=CreateOrderitemSerializer(),
        required=False
    )
    class Meta(BaseOrderSerializer.Meta): ...
