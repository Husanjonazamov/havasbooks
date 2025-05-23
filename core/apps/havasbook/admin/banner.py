from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from ..models import BannerModel


@admin.register(BannerModel)
class BannerAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "__str__",
    )



