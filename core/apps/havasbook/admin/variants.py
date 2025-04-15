from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import ColorModel, SizeModel


@admin.register(ColorModel)
class ColorAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SizeModel)
class SizeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
