from django.urls import URLPattern, path

from baskets import views

app_name = "baskets"

urlpatterns: list[URLPattern] = [
    path(
        "add_to_basket/", 
        views.add_to_basket, 
        name="add_to_basket"
    ),
    path(
        "change_basket/", 
        views.change_basket, 
        name="change_basket"
    ),
    path(
        "remove_from_basket/",
        views.remove_from_basket,
        name="remove_from_basket",
    ),
]
