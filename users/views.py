from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from .forms import CustomLoginForm


def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:home'))
    else:
        form = CustomLoginForm()

    context = {
        'title': 'Home - Авторизація',
        'form': form
    }

    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - Реєстрація'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабінет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {
        'title': 'Home - Вихід'
    }
    return render(request, '', context)
