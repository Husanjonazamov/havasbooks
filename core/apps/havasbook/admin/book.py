from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin, TabularInline

from ..models import BookimageModel, BookModel



class BookimageInline(TabularInline):
    model = BookimageModel
    extra = 1 



@admin.register(BookModel)
class BookAdmin(ModelAdmin, TabbedTranslationAdmin):
    readonly_fields = ("price",)
    list_display = (
        "id",
        "__str__",
        'name',
        'price',
        'is_discount',
        'image'
    )
    
    list_filter = ('is_discount',)
    search_fields = ('original_price',)
    
    fieldsets = (
        (None, {
            'fields': ('original_price', 'discount_percent', 'price', 'is_discount', 'image')
        }),
    )

    def save_model(self, request, obj, form, change):
        if obj.is_discount and obj.discount_percent is not None:
            obj.price = obj.original_price - (obj.original_price * obj.discount_percent / 100)
        else:
            obj.price = obj.original_price  # Chegirma yo'q bo'lsa, original_price'ni saqlaydi
        super().save_model(request, obj, form, change)
        
        
    inlines = [
        BookimageInline,
    ]
   


@admin.register(BookimageModel)
class BookimageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
