from rest_framework import serializers

from ...models import OrderModel, OrderitemModel, OrderStatus
from core.apps.havasbook.serializers.order.orderITem import CreateOrderitemSerializer
from core.apps.havasbook.models.book import BookModel
from core.apps.havasbook.serializers.location import ListLocationSerializer
from core.apps.havasbook.serializers import ListBookSerializer
from .send_order import send_order_to_telegram
from core.apps.havasbook.models.location import LocationModel
from core.apps.havasbook.models.delivery import DeliveryModel
from core.apps.havasbook.serializers.order.orderITem import OrderItemSerializers

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
            'comment',
        ]

class ListOrderSerializer(BaseOrderSerializer):
    order_item = OrderItemSerializers(many=True)  

    class Meta(BaseOrderSerializer.Meta): 
        fields = [
            'id',
            'user',
            "phone",
            'location',
            'delivery_method',
            'payment_method',
            'total_amount',
            'status',
            'comment',
            'order_item' 
        ]




class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...




class CreateOrderSerializer(serializers.ModelSerializer):
    order_item = CreateOrderitemSerializer(many=True)
    delivery_method = serializers.PrimaryKeyRelatedField(queryset=DeliveryModel.objects.all())  # delivery methodni id orqali olish

    class Meta:
        model = OrderModel
        fields = ['phone', 'location', 'delivery_method', 'payment_method', 'total_amount', 'status', 'comment', 'order_item']

    def create(self, validated_data):
        order_item_data = validated_data.pop('order_item', None)
        delivery_method_data = validated_data.pop('delivery_method', None)

        total_price = 0

        user = self.context['request'].user

        # Yangi order yaratish
        order = OrderModel.objects.create(user=user, **validated_data)

        # Delivery methodni olish va saqlash
        try:
            delivery_method_instance = DeliveryModel.objects.get(id=delivery_method_data.id if hasattr(delivery_method_data, 'id') else delivery_method_data)
            order.delivery_method = delivery_method_instance
        except DeliveryModel.DoesNotExist:
            raise serializers.ValidationError(f"Delivery method ID {delivery_method_data} mavjud emas.")

        # Order itemlarni yaratish
        for item_data in order_item_data:
            book = item_data['book']
            quantity = item_data['quantity']

            book_id = book.id if isinstance(book, BookModel) else book

            try:
                book_instance = BookModel.objects.get(id=book_id)
            except BookModel.DoesNotExist:
                raise serializers.ValidationError(f"Kitob ID {book_id} mavjud emas.")

            price = book_instance.price
            item_total = price * quantity
            total_price += item_total

            # Order itemni saqlash
            OrderitemModel.objects.create(
                order=order,
                book=book_instance,
                quantity=quantity,
                price=price 
            )

        order.total_amount = total_price
        order.save()

        location_id = validated_data.get('location')
        try:
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





class OrderStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = [
            'status'
        ]

    def validate_status(self, value):
        valid_statuses = [status.value for status in OrderStatus]
        if value not in valid_statuses:
            raise serializers.ValidationError("Invalid status.")
        return value

