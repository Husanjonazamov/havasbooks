from rest_framework import serializers

from ...models import OrderModel, OrderitemModel
from core.apps.havasbook.serializers.order.orderITem import CreateOrderitemSerializer
from core.apps.havasbook.models.book import BookModel

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



class CreateOrderSerializer(serializers.ModelSerializer):
    order_item = CreateOrderitemSerializer(many=True)  # Bir nechta order_item

    class Meta:
        model = OrderModel
        fields = ['user', 'location', 'delivery_method', 'payment_method', 'total_amount', 'status', 'comment', 'order_item']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_item', None)

        order = OrderModel.objects.create(**validated_data)

        for item_data in order_item_data:
            # book_id ni olish (agar item_data['book'] - bu BookModel obyektidan)
            book_id = item_data['book'].id if isinstance(item_data['book'], BookModel) else item_data['book']

            # Kitob ID mavjudligini tekshirish
            if not BookModel.objects.filter(id=book_id).exists():
                raise serializers.ValidationError(f"Kitob ID {book_id} mavjud emas.")

            # Orderitem yaratish
            OrderitemModel.objects.create(
                order=order,
                book_id=book_id,  # Kitob ID
                quantity=item_data['quantity'],
                price=item_data['price']
            )

        return order


