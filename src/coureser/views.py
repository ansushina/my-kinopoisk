from coureser.forms import LoginForm, RegisterForm, CommentForm
from coureser.models import Film, Profile, Comment
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.


def index(request):
    context = {
        'new_films': Film.objects.new_top(),
        'most_commented': Film.objects.most_commented(),
    }
    return render(request, 'index.html', context=context)


def film(request, fid):
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('/login/')
        form = CommentForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            Comment.objects.create(
                text=cdata['text'],
                author=request.user.profile,
                film_id=fid)
            # todo пагинация
            return redirect('/film/' + str(fid))  # todo правильные редиректы
    else:
        form = CommentForm()
    film = get_object_or_404(Film, pk=fid)
    return render(request, 'film.html', {'film': film, 'form': form})


def login(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            user = auth.authenticate(**cdata)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            form.add_error(None, 'no such user')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    # try https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cdata = form.cleaned_data
            if cdata['password'] == cdata['rep_password']:
                u = User.objects.create_user(
                    username=cdata['username'],
                    email=cdata['email'],
                    password=cdata['password'])
                Profile.objects.create(user=u)

                user = auth.authenticate(**cdata)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/')
                return redirect('/')  # todo правильные редиректы
            else:
                form.add_error('password', ValidationError(('Пароли должны совпадать!'), code='invalid'))
                form.add_error('rep_password', ValidationError(('Пароли должны совпадать!'), code='invalid'))
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')
