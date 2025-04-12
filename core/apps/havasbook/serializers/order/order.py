from rest_framework import serializers

from ...models import OrderModel, OrderitemModel
from core.apps.havasbook.serializers.order.orderITem import CreateOrderitemSerializer
from core.apps.havasbook.models.book import BookModel
from core.apps.havasbook.serializers.location import ListLocationSerializer
from core.apps.havasbook.serializers import ListBookSerializer
from .send_order import send_order_to_telegram
from core.apps.havasbook.models.location import LocationModel

class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = [
            'id',
            'user',
            "phone",
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
        fields = ['user', 'phone', 'location', 'delivery_method', 'payment_method', 'total_amount', 'status', 'comment', 'order_item']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_item', None)

        # Order yaratish
        order = OrderModel.objects.create(**validated_data)

        # Order item larini yaratish
        for item_data in order_item_data:
            book = item_data['book']
            book_id = book.id if isinstance(book, BookModel) else book

            # Kitobning mavjudligini tekshirish
            if not BookModel.objects.filter(id=book_id).exists():
                raise serializers.ValidationError(f"Kitob ID {book_id} mavjud emas.")

            # Order item yaratish
            OrderitemModel.objects.create(
                order=order,
                book_id=book_id,
                quantity=item_data['quantity'],
                price=item_data['price']
            )

        # Location olish va Telegramga yuborish
        location_id = validated_data.get('location')
        try:
            # Location topish
            location = LocationModel.objects.get(id=location_id.id if hasattr(location_id, 'id') else location_id)
            send_order_to_telegram(
                order=order,
                location_name=location.name,
                latitude=location.latitude,
                longitude=location.longitude
            )
        except LocationModel.DoesNotExist:
            print("Location topilmadi, Telegramga yuborilmadi.")

        return order
