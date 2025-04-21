from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import LocationModel


@admin.register(LocationModel)
class LocationAdmin(ModelAdmin):
    list_display = (
        "id",
        'title',
        'long',
        'lat'
    )
