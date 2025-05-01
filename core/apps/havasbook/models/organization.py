# from django.db import models
from core.http.models import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


class OrganizationModel(AbstractBaseModel):
    name = ...

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("OrganizationModel")
        verbose_name_plural = _("OrganizationModel")
