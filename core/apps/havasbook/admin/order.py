from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import OrderitemModel, OrderModel


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(OrderitemModel)
class OrderitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
