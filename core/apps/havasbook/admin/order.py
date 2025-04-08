from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import OrderitemModel, OrderModel


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
        'user_name',
        'payment_method',
        'total_amount',
        'status'
    )
    
    def user_name(self, obj):
        return obj.user.first_name


@admin.register(OrderitemModel)
class OrderitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
        'order',
        'book',
        'price'
    )
    
    def order(self, obj):
        return obj.order.user.first_name
    
    def book(self, obj):
        return obj.book.name
