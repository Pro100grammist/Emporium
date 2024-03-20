from django.urls import URLPattern, path

from assortment import views

app_name = "assortment"

urlpatterns: list[URLPattern] = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
]
