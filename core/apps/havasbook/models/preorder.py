from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.accounts.models import User



class Status(models.TextChoices):
        NEW = 'yangi', _('Yangi')
        ACCEPTED = 'qabul qilindi', _('Qabul qilindi')
        CANCELLED = 'bekor qilindi', _('Bekor qilindi')



class PreorderModel(AbstractBaseModel):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="preorder"
    )
    book = models.ForeignKey(
        'havasbook.BookModel',
        on_delete=models.CASCADE,
        related_name="book"
    )
    count = models.PositiveIntegerField(
        _("Mahlulot Soni"),
        default=1
    )
    user_name = models.CharField(
        _("Foydalanuvchi ismi"),
        max_length=250, 
        null=True,
        blank=True
    )
    phone = models.CharField(
        _("Telefon raqam"),
        max_length=100,
        null=True,
        blank=True
    )

    status = models.CharField(
        _("Status"),
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    def __str__(self):
        return self.book.name



    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "preorder"
        verbose_name = _("PreorderModel")
        verbose_name_plural = _("PreorderModels")
