from django import template

from baskets.models import Basket
from baskets.utils import get_user_carts

register = template.Library()


@register.simple_tag()
def carts(request):
    return get_user_carts(request)
