from django.db import models
from django.urls import reverse

from users.models import User
from assortment.models import Products


class BasketQueryset(models.QuerySet):

    def total_price(self):
        return sum([basket.price() for basket in self])
    
    def total_quantity(self):
        return sum(basket.amount for basket in self) if self else 0


class Basket(models.Model):

    user = models.ForeignKey(to=User, blank=True, null=True, verbose_name="Покупець", on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, verbose_name="Товар", on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=0, verbose_name="Кількість")
    session_key = models.CharField(max_length=32, blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    class Meta:
        verbose_name = "Basket"
        verbose_name_plural = "Baskets"
    
    objects = BasketQueryset().as_manager()

    def __str__(self):
        if self.user:
            return f'Корзина {self.user.username} | Товар {self.product.name} | Кількість {self.amount}'
        else:
            return f'Корзина без користувача | Товар {self.product.name} | Кількість {self.amount}'

    def get_absolute_url(self):
        return reverse("Basket_detail", kwargs={"pk": self.pk})
    
    def price(self):
        return round(self.product.discount_price() * self.amount, 2)
