from rest_framework import serializers

from ...models import OrderitemModel


class BaseOrderitemSerializer(serializers.ModelSerializer):
    order = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()
    class Meta:
        model = OrderitemModel
        fields = [
            'id',
            'order',
            'book',
            'quantity',
            'price'
        ]

    def get_order(self, obj): 
        from core.apps.havasbook.serializers.order import ListOrderSerializer
        return ListOrderSerializer(obj.order).data
    
    def get_book(self, obj):
        from core.apps.havasbook.serializers.book import ListBookSerializer
        return ListBookSerializer(obj.book).data
    


class ListOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class RetrieveOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class CreateOrderitemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderitemModel
        fields = [
            'book',
            'quantity',
            'price',
        ]
