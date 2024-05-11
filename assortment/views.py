from django.shortcuts import render
from django.template import context

from .models import Products


def catalog(request):

    goods = Products.objects.all()

    context = {
        "title": "Emporium - Catalog",
        "goods": goods
    }
    return render(request, "assortment/catalog.html", context=context)


def product(request):
    return render(request, "assortment/product.html")
