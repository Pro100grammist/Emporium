from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.db.models import F

from users.models import User


class CustomLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

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
    #                                       })
    # )


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    # fist_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть ваше ім'я"
    #         }
    #     )
    # )
    #
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть ваше прізвище"
    #         }
    #     )
    # )
    #
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть iм'я користувача"
    #         }
    #     )
    # )
    #
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть вашу електронну пошту"
    #         }
    #     )
    # )
    #
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть ваш пароль"
    #         }
    #     )
    # )
    #
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Підтвердіть ваш пароль"
    #         }
    #     )
    # )


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        )

    # compact version
    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

    # """extended version"""
    #
    # image = forms.ImageField(
    #     widget=forms.FileInput(
    #         attrs={
    #             "class": "form-control mt-3"
    #         }
    #     ),
    #     required=False
    # )
    #
    # fist_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть ваше ім'я"
    #         }
    #     )
    # )
    #
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть ваше прізвище"
    #         }
    #     )
    # )
    #
    # username = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть iм'я користувача"
    #         }
    #     )
    # )
    #
    # email = forms.CharField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введіть вашу електронну пошту"
    #         }
    #     )
    # )


