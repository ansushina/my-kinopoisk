from coureser.forms import LoginForm, RegisterForm, CommentForm, SettingsForm, SearchForm, LikeForm
from coureser.models import Film, Profile, Comment, Like
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View, FormView, DetailView


# Create your views here.
def paginate(objects_list, request, page_size=10):
    # do smth with Paginator, etc…

    paginator = Paginator(objects_list, page_size)
    page = request.GET.get('page')
    # №objects_page = paginator.page()
    objects_page = paginator.get_page(page)

    return objects_page, paginator


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['new_films'] = Film.objects.new_top()
        context['most_commented'] = Film.objects.most_commented()
        return context


class SearchView(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        querydict = self.request.GET
        films = Film.objects.search_with_filters(querydict)
        films, p = paginate(films, self.request, 20)
        context['films'] = films
        context['form'] = self.form_class(querydict)
        return context


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')


class FilmView(FormView, DetailView):
    form_class = CommentForm
    template_name = 'film.html'
    model = Film

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        cdata = form.cleaned_data
        Comment.objects.create(
            text=cdata['text'],
            author=self.request.user.profile,
            film_id=self.kwargs['pk'])
        comments = Comment.objects.filter(film__id=self.kwargs['pk'])
        comments, p = paginate(comments, self.request, 20)
        return redirect('/film/' + str(self.kwargs['pk']) + '/' + '?page='+str(p.num_pages) + '#paginated')  # todo правильные редиректы

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        like = Like.objects.filter(film_id=self.kwargs['pk'], author_id=self.request.user.id).first()
        if like:
            likedata = {'value':like.value}
        else:
            likedata = {}
        context['form_like'] = LikeForm(likedata)
        context['comments'], p = paginate(context['film'].comment_set.all(), self.request, 20)
        return context


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('/')  # todo равильные редиректы
        cdata = form.cleaned_data
        user = auth.authenticate(**cdata)
        if user is not None:
            auth.login(self.request, user)
            return redirect('/')
        form.add_error(None, 'no such user')
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('/')  # todo равильные редиректы
        cdata = form.cleaned_data
        if cdata['password'] == cdata['rep_password']:
            u = User.objects.create_user(
                username=cdata['username'],
                email=cdata['email'],
                password=cdata['password'])
            Profile.objects.create(user=u)

            user = auth.authenticate(**cdata)
            if user is not None:
                auth.login(self.request, user)
                return redirect('/')
            return redirect('/')  # todo правильные редиректы
        else:
            form.add_error('password', ValidationError(('Пароли должны совпадать!'), code='invalid'))
            form.add_error('rep_password', ValidationError(('Пароли должны совпадать!'), code='invalid'))

        return self.render_to_response(self.get_context_data(form=form))


class SettingsView(FormView):
    form_class = SettingsForm
    template_name = 'settings.html'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        form = SettingsForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            cdata = form.cleaned_data
            print(cdata)
            Profile.objects.update(self.request.user, cdata)
            return redirect('/')


class LikeView(FormView):
    form_class = LikeForm

    def form_valid(self, form):
        print(self.kwargs['pk'])
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        cdata = form.cleaned_data
        answer = Like.objects.like(cdata['value'], self.kwargs['pk'], self.request.user)
        Film.objects.count_rating(self.kwargs['pk'])
        return redirect('/film/' + str(self.kwargs['pk']))
