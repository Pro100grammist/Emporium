from django.shortcuts import render
from django.template import context

from .data import goods


def catalog(request):
    context = {"title": "Emporium - Catalog", "goods": goods}
    return render(request, "assortment/catalog.html", context=context)


def product(request):
    return render(request, "assortment/product.html")
