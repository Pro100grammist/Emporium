from re import I
from django.db.models import Manager
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render
from django.template import context

from .models import Products


def catalog(request, category_slug) -> HttpResponse:

    page = request.GET.get('page', 1)

    if category_slug == "interior":
        goods: Manager[Products] = Products.objects.all()
    else:
        goods: Manager[Products] = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, per_page=6)
    current_page = paginator.page(int(page))

    context = {
        "title": "Emporium - Catalog",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "assortment/catalog.html", context=context)


def product(request, product_slug) -> HttpResponse:

    product: Products = Products.objects.get(slug=product_slug)

    context: dict[str, Products] = {
        'product': product
    }

    return render(request, "assortment/product.html", context=context)
