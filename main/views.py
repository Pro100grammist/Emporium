from re import T
from django.http import HttpResponse
from django.shortcuts import render


def index(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Головна',
        'brandname': 'EMPORIUM',
        'content': 'Магазин антикварного інтер\'єру',
    }
    return render(request, 'main/index.html', context)


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        "title": "Home - Про нас",
        "content": "Про нас",
        'text_on_page': "Emporium - це інтернет магазин вишуканих антикварних меблів та предметів інтер'єру."
    }
    return render(request, "main/about.html", context)
