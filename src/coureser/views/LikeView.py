from django.shortcuts import redirect
from django.views.generic import FormView

from coureser.forms.LikeForm import LikeForm
from coureser.models.Film import Film
from coureser.models.Like import Like


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