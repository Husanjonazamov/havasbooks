from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect
from unfold.admin import ModelAdmin
from django.utils.html import format_html

from ..models import OrderitemModel, OrderModel
from django.shortcuts import get_object_or_404, redirect

from ..format_html.order import (
    colored_id,
    order_images,
    colored_status,
    mark_ready_button
)



@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        colored_id,
        order_images,
        "reciever_name",
        "reciever_phone",
        'payment_method',
        'total_price',
        colored_status,
        mark_ready_button,
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:order_id>/mark-ready/', self.admin_site.admin_view(self.mark_ready), name='order-mark-ready'),
        ]
        return custom_urls + urls

    def mark_ready(self, request, order_id):
        order = get_object_or_404(OrderModel, pk=order_id)
        if order.status != 'ready':
            order.status = 'ready'
            order.save()
            self.message_user(request, f"Buyurtma #{order.id} tayyor bo‘ldi.", messages.SUCCESS)
        else:
            self.message_user(request, f"Buyurtma #{order.id} allaqachon tayyor.", messages.WARNING)
        return redirect(f"../../{order_id}/change/")
    



@admin.register(OrderitemModel)
class OrderitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "get_order_user",
        'get_book_name',
        "quantity",
        'price'
    )

    def get_order_user(self, obj):
        return obj.order.reciever_name
    get_order_user.short_description = "Buyurtmachi"

    def get_book_name(self, obj):
        return obj.book.name
    get_book_name.short_description = "Kitob"
