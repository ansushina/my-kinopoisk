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
