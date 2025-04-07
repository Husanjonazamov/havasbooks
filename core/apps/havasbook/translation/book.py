from modeltranslation.translator import TranslationOptions, register

from ..models import BookModel


@register(BookModel)
class BookTranslation(TranslationOptions):
    fields = []
