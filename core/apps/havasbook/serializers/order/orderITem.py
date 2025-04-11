from rest_framework import serializers

from ...models import OrderitemModel
from core.apps.havasbook.models.book import BookModel

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



class CreateOrderitemSerializer(serializers.Serializer):
    book = serializers.IntegerField()  
    quantity = serializers.IntegerField(default=1) 
    price = serializers.DecimalField(max_digits=10, decimal_places=2)  

    def validate_book(self, value):
        """ Kitob ID ning mavjudligini tekshiradi """
        if not BookModel.objects.filter(id=value).exists():
            raise serializers.ValidationError(f"Kitob ID {value} mavjud emas.")
        return value

    class Meta:
        fields = ['book', 'quantity', 'price']
