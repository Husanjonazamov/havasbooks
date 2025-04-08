from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.accounts.models.user import User


class CartModel(AbstractBaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="Foydalanuvchi"
    )
    total_price = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        default=0.00
    )
    
    def __str__(self):
        return self.user.first_name
    
    def update_total_price(self):
        """Umumiy narxni yangilash."""
        total = sum(item.total_price for item in self.items.all())  
        self.total_price = total
        self.save()

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "cart"
        verbose_name = _("CartModel")
        verbose_name_plural = _("CartModels")


class CartitemModel(AbstractBaseModel):
    cart = models.ForeignKey(
        CartModel,
        on_delete=models.CASCADE,
        related_name="items"
    )
    book = models.ForeignKey(
        'havasbook.BookModel',
        on_delete=models.CASCADE
    )
    quantity = models.PositiveBigIntegerField(_("Mahsulot soni"), default=1)
    total_price = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=0.00
    )
    
    def save(self, *args, **kwargs):
        """Kitobning umumiy narxini hisoblash."""
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)
        self.cart.update_total_price()
         
         
    def update_total_price(self):
        """Umumiy narxni yangilash."""
        total = sum(item.total_price for item in self.items.all())  
        self.total_price = total  
        self.save()    
    

    def __str__(self):
        return self.book.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="Test",
        )

    class Meta:
        db_table = "cartItem"
        verbose_name = _("CartitemModel")
        verbose_name_plural = _("CartitemModels")
