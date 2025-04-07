from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BannerModel(AbstractBaseModel):
    name = models.CharField(_("Nomi"), max_length=255)
    image = models.ImageField(_("Rasm"), upload_to="banner-image/")    
    
    def __str__(self):
        return self.name or 'banner Item'

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "banner"
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModels")


