from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse

from .forms import CustomLoginForm, UserRegistrationForm


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
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'Home - Реєстрація',
        'form': form
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабінет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)

    context = {
        'title': 'Home - Вихід'
    }
    return redirect(reverse('main:home'))
