from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BannerimageModel, BannerModel


@admin.register(BannerModel)
class BannerAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(BannerimageModel)
class BannerimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
