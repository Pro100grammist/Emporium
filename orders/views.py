from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render

from orders.models import UserOrder, OrderItem

from baskets.models import Basket
from orders.forms import CreateOrderForm


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    basket_items = Basket.objects.filter(user=user)

                    if basket_items.exists():
                        order = UserOrder.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            requires_delivery=form.cleaned_data["requires_delivery"],
                            delivery_address=form.cleaned_data["delivery_address"],
                            cash_on_delivery=form.cleaned_data["cash_on_delivery"],
                        )

                        for basket_item in basket_items:
                            product = basket_item.product
                            name = product.name
                            price = basket_item.price()
                            amount = basket_item.amount

                            if product.amount < amount:
                                raise ValidationError(f'{name} в наявності на складі - {product.amount}')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                amount=amount
                            )

                            product.amount -= amount
                            product.save()

                        basket_items.delete()

                        messages.success(request, "Замовлення прийнято!")
                        return redirect('user:profile')
            except ValidationError as e:
                messages.success(request, str(e))
                return redirect('orders:create_order')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        }

        form = CreateOrderForm(initial=initial)

    context = {
        'title': 'Emporium - Оформлення замовлення',
        'form': form
    }

    return render(request, 'orders/create_order.html', context=context)

