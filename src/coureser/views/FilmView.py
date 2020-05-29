from django.shortcuts import redirect
from django.views.generic import FormView, DetailView

from coureser.common.paginator import paginate
from coureser.forms.CommentForm import CommentForm
from coureser.forms.LikeForm import LikeForm
from coureser.models.Comment import Comment
from coureser.models.Film import Film
from coureser.models.Like import Like


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
        comments, p = paginate(comments, self.request)
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