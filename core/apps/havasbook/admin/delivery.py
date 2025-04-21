from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import DeliveryModel


@admin.register(DeliveryModel)
class DeliveryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
