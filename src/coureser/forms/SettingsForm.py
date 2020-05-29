from django import forms

from coureser.common.constants import error_username


class SettingsForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        max_length=20,
        min_length=2,
        error_messages=error_username,
        required=False,
    )
    email = forms.EmailField(required=False)
    avatar = forms.ImageField(
        required=False,
        label="Изменить аватар"
    )