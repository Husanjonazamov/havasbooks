from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BannerModel(AbstractBaseModel):
    name = models.CharField(_("Nomi"), max_length=255)
    price = models.DecimalField(
        max_digits=10,     
        decimal_places=2,   
        default=0.00,      
        verbose_name="Narx"
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name="Chegirma foizi",
        help_text="Chegirma foizini kiriting"
    )

    image = models.ImageField(_("Rasm"), upload_to="banner-product/")
    
    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "banner"
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModels")


