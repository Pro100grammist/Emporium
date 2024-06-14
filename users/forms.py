from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User


class CustomLoginForm(AuthenticationForm):

    # Option 1: for the variant with processing the login form through the front
    username = forms.CharField()
    password = forms.CharField()

    # Option 2: for the variant with processing the login form through the backend
    # username = forms.CharField(
    #     label="Ім'я користувача",
    #     widget=forms.TextInput(attrs={"autofocus": True,
    #                                   "class": "form-control",
    #                                   "placeholder": "Введіть ім'я користувача",
    #                                   }))
    #
    # password = forms.CharField(
    #     label="Пароль",
    #     widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
    #                                       "class": "form-control",
    #                                       "placeholder": "Введіть пароль",
    #                                       }),
    # )

    class Meta:
        model = User
        fields = ['username', 'password']
