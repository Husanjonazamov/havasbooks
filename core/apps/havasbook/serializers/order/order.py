from rest_framework import serializers

from ...models import OrderModel, OrderitemModel, OrderStatus
from core.apps.havasbook.serializers.order.orderITem import CreateOrderitemSerializer
from core.apps.havasbook.models.book import BookModel
from core.apps.havasbook.serializers.location import CreateLocationSerializer
from core.apps.havasbook.serializers import ListBookSerializer
from .send_order import send_order_to_telegram
from core.apps.havasbook.models.location import LocationModel
from core.apps.havasbook.models.delivery import DeliveryModel
from core.apps.havasbook.serializers.order.orderITem import OrderItemSerializers, ListOrderItemSerializers
from core.apps.havasbook.models.cart import CartitemModel, CartModel

class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = [
            'id',
            'user',
            "reciever_phone",
            'location',
            'delivery_method',
            'payment_method',
            'total_price',
            'status',
            'comment',
        ]

class ListOrderSerializer(BaseOrderSerializer):
    order_item = ListOrderItemSerializers   (many=True)  
    location = serializers.SerializerMethodField()
    delivery_price = serializers.SerializerMethodField()

    class Meta(BaseOrderSerializer.Meta): 
        fields = [
            'id',
            "reciever_phone",
            "reciever_name",
            'location',
            'delivery_price',
            'delivery_method',
            'payment_method',
            'total_price',
            'status',
            'comment',
            'order_item' 
        ]
        
        
    def get_delivery_price(self, obj):
        return obj.delivery_method.price
        
    def get_location(self, obj):
        return obj.location.title if obj.location else None
        



class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...




class CreateOrderSerializer(serializers.ModelSerializer):
    location = CreateLocationSerializer()
    order_item = CreateOrderitemSerializer(many=True)
    delivery_method = serializers.PrimaryKeyRelatedField(queryset=DeliveryModel.objects.all())
    reciever = serializers.DictField(write_only=True)

    class Meta:
        model = OrderModel
        fields = [
            'location',
            'delivery_method',
            'reciever',
            'payment_method',
            'comment',
            'order_item'
        ]

    def create(self, validated_data):
        location_data = validated_data.pop('location')
        order_items_data = validated_data.pop('order_item')
        reciever_data = validated_data.pop('reciever')

        user = self.context['request'].user

        location = LocationModel.objects.create(**location_data)
        delivery_method = validated_data['delivery_method']
        delivery_price = delivery_method.price

        order = OrderModel.objects.create(
            user=user,
            location=location,
            delivery_method=delivery_method,
            payment_method=validated_data.get('payment_method'),
            comment=validated_data.get('comment'),
            reciever_name=reciever_data['name'],
            reciever_phone=reciever_data['phone'],
        )

        total_price = 0
        for item in order_items_data:
            book_id = item['book'] if isinstance(item['book'], int) else item['book'].id
            book = BookModel.objects.get(id=book_id)
            price = book.price
            quantity = item['quantity']
            OrderitemModel.objects.create(
                order=order,
                book=book,
                quantity=quantity,
                price=price
            )
            total_price += price * quantity

        total_price += delivery_price
        order.total_amount = total_price
        order.save()

        cart = CartModel.objects.filter(user=user).first()
        if cart:
            CartitemModel.objects.filter(cart=cart).delete()


        send_order_to_telegram(
            order=order,
            location_name=location.title,
            latitude=location.lat,
            longitude=location.long
        )

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

