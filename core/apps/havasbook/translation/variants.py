from modeltranslation.translator import TranslationOptions, register

from ..models import ColorModel, SizeModel


@register(ColorModel)
class ColorTranslation(TranslationOptions):
    fields = []


@register(SizeModel)
class SizeTranslation(TranslationOptions):
    fields = []
