from django.db import models
from django.core.validators import validate_email
from assortment.models import Products

from users.models import User


class OrderItemQuerySet(models.QuerySet):

    def total_price(self):
        return sum(basket.price() for basket in self)

    def total_quantity(self):
        if self:
            return sum(basket.amount for basket in self)
        return 0


class UserOrder(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name='Користувач', default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата замовлення')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    requires_delivery = models.BooleanField(default=False, verbose_name='Доставка')
    delivery_address = models.TextField(null=True, blank=True, verbose_name='Адреса доставки')
    cash_on_delivery = models.BooleanField(default=False, verbose_name='Оплата при отриманні')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.CharField(max_length=50, default='Комплектується', verbose_name='Статус замовлення')

    class Meta:
        db_table = 'order'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Замовлення № {self.pk} | Покупець {self.user.first_name} {self.user.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(to=UserOrder, on_delete=models.CASCADE, verbose_name='Замовлення')
    product = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, null=True, verbose_name='Товар', default=None)
    name = models.CharField(max_length=150, verbose_name='Найменування')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Ціна')
    amount = models.PositiveIntegerField(default=0, verbose_name='Кількість')
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата придбання')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Sold product'
        verbose_name_plural = 'Sold products'

    objects = OrderItemQuerySet.as_manager()

    def products_price(self):
        return round(self.price * self.amount, 2)

    def __str__(self):
        return f'Товар {self.name} | Замовлення № {self.order.pk}'

