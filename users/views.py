from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse

from users.forms import CustomLoginForm, UserRegistrationForm, ProfileForm
from baskets.models import Basket


def login(request):

    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Ви увійшли до свого акаунту")

                if session_key:
                    Basket.objects.filter(session_key=session_key.update(user=user))

                redirect_page = request.POST.get('next', None)

                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.GET.get('next'))
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
            session_key = request.session.session_key
            user = form.instance

            if session_key:
                Basket.objects.filter(session_key=session_key).update(user=user)

            auth.login(request, user)
            messages.success(request, f"{user.username}, реєстрація на сайті пройшла успішно!")
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Home - Реєстрація',
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Ваш профайл успішно обновлено.")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserRegistrationForm(instance=request.user)

    context = {
        'title': 'Home - Кабінет',
        'form': form
    }
    return render(request, 'users/profile.html', context)


@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Ви щойно вийшли зі свого акаунту.")
    auth.logout(request)

    context = {
        'title': 'Home - Вихід'
    }
    return redirect(reverse('main:home'))


def cart(request):
    return render(request, 'users/cart.html')