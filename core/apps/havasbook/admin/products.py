from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import ProductsimageModel, ProductsModel


@admin.register(ProductsModel)
class ProductsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(ProductsimageModel)
class ProductsimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
