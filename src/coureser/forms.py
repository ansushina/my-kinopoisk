from coureser.models import Genre, Actor, Country
from django import forms

error_username = {
    'required': 'Пожалуйста, заполните это поле!',
    'max_length': 'Имя не может превышать 20 символов!',
    'min_length': 'Имя должно быть больше 2 символов!'
}


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        max_length=20,
        min_length=2,
        error_messages=error_username,
    )
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


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


class CommentForm(forms.Form):
    text = forms.CharField(
        label="Напишите что-нибудь",
        required=False,
        widget=forms.Textarea(attrs={'rows': '5'})
    )


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


class SearchForm(forms.Form):
    q = forms.CharField(label="Название", required=False)
    genre = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Genre.objects.all(),
        required=False,
        label="Жанры"
    )
    country = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Country.objects.all(),
        required=False,
        label="Страны"
    )
    actor = forms.ModelMultipleChoiceField(
        widget=forms.SelectMultiple,
        queryset=Actor.objects.all().order_by('firstName'),
        required=False,
        label="Актеры"
    )
    year_from = forms.IntegerField(min_value=1930, max_value=2020, label="Год от", required=False, )
    year_to = forms.IntegerField(min_value=1930, max_value=2020, label="До", required=False, )


class LikeForm(forms.Form):
    value = forms.ChoiceField(
        choices=(
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        ),
        label="Оцените фильм",
        required=False,
        widget=forms.RadioSelect,
    )
