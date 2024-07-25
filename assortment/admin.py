from django.contrib import admin

from .models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    fields = ["name", "category", "slug", "description", "image", ("price", "discount", "amount")]
    list_display = ['name', 'amount', 'price', 'discount']
    list_editable = ['amount', 'price', 'discount']
    search_fields = ['name', 'description']
    list_filter = ['amount', 'discount', 'category']


