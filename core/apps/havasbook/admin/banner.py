from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BannerModel


@admin.register(BannerModel)
class BannerAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
