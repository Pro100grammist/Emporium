from django.urls import URLPattern, path

from baskets import views

app_name = "baskets"

urlpatterns: list[URLPattern] = [
    path(
        "add_to_basket/<slug:product_slug>/", 
        views.add_to_basket, 
        name="add_to_basket"
    ),
    path(
        "change_basket/<slug:product_slug>/", 
        views.change_basket, 
        name="change_basket"
    ),
    path(
        "remove_from_basket/<slug:product_slug>/",
        views.remove_from_basket,
        name="remove_from_basket",
    ),
]
