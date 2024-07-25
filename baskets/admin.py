from django.contrib import admin

from baskets.models import Basket

# admin.site.register(Basket)
FIELDS = 'product', 'amount', 'created_timestamp'


class BasketTabAdmin(admin.TabularInline):
    model = Basket
    fields = FIELDS
    search_fields = FIELDS
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'amount', 'created_timestamp']
    list_filter = ['created_timestamp', 'user', 'product__name']

    def product_display(self, obj):
        return str(obj.product.name)
    