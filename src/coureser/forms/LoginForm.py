from django import forms

from coureser.common.constants import error_username


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        max_length=20,
        min_length=2,
        error_messages=error_username,
    )
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")