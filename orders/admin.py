from django.contrib import admin

from orders.models import UserOrder, OrderItem


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "amount"
    search_fields = ("product", "name")
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "amount"
    search_fields = ("order", "product", "name")


class OrderTabularAdmin(admin.TabularInline):
    model = UserOrder
    fields = ("requires_delivery", "status", "cash_on_delivery", "is_paid", "created_timestamp")
    search_fields = ("requires_delivery", "cash_on_delivery", "is_paid", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(UserOrder)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "requires_delivery", "status", "cash_on_delivery", "is_paid", "created_timestamp")
    list_filter = ("requires_delivery", "cash_on_delivery", "is_paid", "created_timestamp")
    search_fields = ("id", "requires_delivery", "cash_on_delivery", "is_paid", "created_timestamp")
    readonly_fields = ("created_timestamp",)
    inlines = (OrderItemTabularAdmin,)
