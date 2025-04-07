from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BookModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)
    original_price = models.DecimalField(
        _("price"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    discount_percent = models.DecimalField(
        _("chegirma foizi"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    is_discount = models.BooleanField(_("Chegirma bormi ?"), default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.discount_percent is not None:  # Agar chegirma bor bo'lsa
            self.final_price = self.original_price - (self.original_price * self.discount_percent / 100)
        else:
            self.price = self.original_price
        super().save(*args, **kwargs)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "book"
        verbose_name = _("BookModel")
        verbose_name_plural = _("BookModels")


class BookimageModel(AbstractBaseModel):
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "bookImage"
        verbose_name = _("BookimageModel")
        verbose_name_plural = _("BookimageModels")
