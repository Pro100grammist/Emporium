from ast import mod
from email.policy import default
from enum import unique
from re import M, T
from tabnanny import verbose
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Product group'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='assortment_images', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.DecimalField(default=0, max_digits=2, decimal_places=0)
    amount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'

    def display_id(self):
        return f'{self.id:05}'

    def discount_price(self):
        return round(self.price * (1 - self.discount / 100), 2) if self.discount else self.price

    def __str__(self):
        return f'{self.name} Amount : {self.amount}'
