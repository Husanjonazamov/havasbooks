from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class LocationModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "location"
        verbose_name = _("LocationModel")
        verbose_name_plural = _("LocationModels")
