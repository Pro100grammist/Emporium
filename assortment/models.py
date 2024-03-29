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

