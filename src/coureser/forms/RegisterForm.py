from django import forms

from coureser.common.constants import error_username


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        max_length=20,
        min_length=2,
        error_messages=error_username,
    )
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Пароль",
    )
    rep_password = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput,
    )