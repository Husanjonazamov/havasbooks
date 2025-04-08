from modeltranslation.translator import TranslationOptions, register

from ..models import CartModel


@register(CartModel)
class CartTranslation(TranslationOptions):
    fields = []
