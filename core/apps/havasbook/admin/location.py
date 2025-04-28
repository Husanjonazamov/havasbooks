from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import LocationModel
from modeltranslation.admin import TabbedTranslationAdmin



@admin.register(LocationModel)
class LocationAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        'title',
        'long',
        'lat'
    )
