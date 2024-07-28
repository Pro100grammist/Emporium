from django.contrib import admin

from .models import User
from baskets.admin import BasketTabAdmin
from orders.admin import OrderTabularAdmin
# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['username', 'first_name', 'last_name', 'email']

    inlines = [BasketTabAdmin, OrderTabularAdmin]
