from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import CartitemModel, CartModel


@admin.register(CartModel)
class CartAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CartitemModel)
class CartitemAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
