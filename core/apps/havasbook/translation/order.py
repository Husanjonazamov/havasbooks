from modeltranslation.translator import TranslationOptions, register

from ..models import OrderModel


@register(OrderModel)
class OrderTranslation(TranslationOptions):
    fields = []
