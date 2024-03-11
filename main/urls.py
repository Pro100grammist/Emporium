from django.urls import path, URLResolver

from main import views

app_name = "main"

urlpatterns: list[URLResolver] = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
]
