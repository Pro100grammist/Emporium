from django.shortcuts import render, redirect

from assortment.models import Products
from baskets.models import Basket

def add_to_basket(request, product_slug):
    
    product = Products.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.amount += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, amount=1)

    return redirect(request.META['HTTP_REFERER'])


def change_basket(request, product_slug): ...


def remove_from_basket(request, product_slug): ...
