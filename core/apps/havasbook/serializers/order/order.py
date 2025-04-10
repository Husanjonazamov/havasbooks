from rest_framework import serializers

from ...models import OrderModel, OrderitemModel
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
    order_item = serializers.ListField(
        child=CreateOrderitemSerializer(),
        required=False
    )

    class Meta(BaseOrderSerializer.Meta):
        fields = BaseOrderSerializer.Meta.fields + ['order_item']  

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_item')

        order = OrderModel.objects.create(**validated_data)

        for item_data in order_item_data:
            OrderitemModel.objects.create(order=order, **item_data)

        return order
