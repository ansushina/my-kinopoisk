from coureser.forms.CommentForm import CommentForm
from coureser.forms.LikeForm import LikeForm
from coureser.models.Film import Film
from django.shortcuts import redirect
from django.views.generic import FormView, DetailView

from coureser.logic.CommentLogic import CommentLogic
from coureser.logic.LikeLogic import LikeLogic


class FilmView(FormView, DetailView):
    form_class = CommentForm
    template_name = 'film.html'
    model = Film

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/login/')

        cdata = form.cleaned_data
        CommentLogic.comment(cdata['text'], self.request.user, self.kwargs['pk'])
        comments, page = CommentLogic.paginate(self.request, self.kwargs['pk'])
        return redirect('/film/' + str(self.kwargs['pk']) + '/' + '?page=' + str(page) + '#paginated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_like'] = LikeForm(LikeLogic.get_like_data(self.kwargs['pk'], self.request.user))
        context['comments'], p = CommentLogic.paginate(self.request, self.kwargs['pk'])
        return context
