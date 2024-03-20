from django.urls import URLPattern, path

from main import views

app_name = "main"

urlpatterns: list[URLPattern] = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
]
