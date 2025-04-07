from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import BookModel
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(BookModel)
class BookAdmin(ModelAdmin, TabbedTranslationAdmin):
    readonly_fields = (
        "price",
    )
    list_display = (
        "id",
        "__str__",
    )
    
    def save_model(self, request, obj, form, change):
        if obj.is_discount and obj.discount_percent is not None:
            obj.price = obj.original_price - (obj.original_price * obj.discount_percent / 100)
        else:
            obj.price = obj.original_price  # Chegirma yo'q bo'lsa, original_price'ni saqlaydi
        super().save_model(request, obj, form, change)
