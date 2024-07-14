from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from assortment.models import Products
from baskets.models import Basket
from baskets.templatetags.carts_tags import carts
from baskets.utils import get_user_carts


def add_to_basket(request):

    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user, product=product)

        if baskets.exists():
            basket = baskets.first()
            if basket:
                basket.amount += 1
                basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, amount=1)

    cart = get_user_carts(request)
    basket_item_html = render_to_string(
        "includes/included_basket.html", {"baskets": cart}, request=request
    )

    response_data = {
        "message": "Товар додано до корзини",
        "cart_items_html": basket_item_html,
    }

    return JsonResponse(response_data)


def change_basket(request):
    basket_id = request.POST.get("basket_id")
    amount = request.POST.get("amount")
    basket = Basket.objects.get(id=basket_id)
    basket.amount = amount
    basket.save()
    cart = get_user_carts(request)
    basket_item_html = render_to_string(
        "includes/included_basket.html", {"baskets": cart}, request=request
    )

    response_data = {
        "message": "Кількість змінено",
        "cart_items_html": basket_item_html,
        "quantity": basket.amount,
    }

    return JsonResponse(response_data)


def remove_from_basket(request):
    basket_id = request.POST.get("basket_id")
    basket = Basket.objects.get(id=basket_id)
    amount = basket.amount
    basket.delete()

    cart = get_user_carts(request)
    basket_item_html = render_to_string(
        "includes/included_basket.html", {"baskets": cart}, request=request
    )

    response_data = {
        "message": "Товар видалено",
        "cart_items_html": basket_item_html,
        "quantity_deleted": amount,
    }

    return JsonResponse(response_data)
