from django.urls import URLPattern, path

from assortment import views

app_name = "assortment"

urlpatterns: list[URLPattern] = [
    path("<slug:category_slug>/", views.catalog, name="index"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
