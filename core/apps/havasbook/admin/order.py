from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import OrderitemModel, OrderModel


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        'payment_method',
        'total_amount',
        'status'
    )




@admin.register(OrderitemModel)
class OrderitemAdmin(ModelAdmin):
    list_display = (
        "id",
        'order',
        'book',
        'price'
    )
    
    def order(self, obj):
        return obj.order.user.first_name
    
    def book(self, obj):
        return obj.book.name
