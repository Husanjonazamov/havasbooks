from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BookModel


@admin.register(BookModel)
class BookAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
