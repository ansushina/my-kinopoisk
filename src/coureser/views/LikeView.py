from django.shortcuts import redirect
from django.views.generic import FormView

from coureser.forms.LikeForm import LikeForm
from coureser.models.Film import Film
from coureser.models.Like import Like

from src.coureser.logic.LikeLogic import LikeLogic


class LikeView(FormView):
    form_class = LikeForm

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        LikeLogic.set_like(form.cleaned_data,  self.kwargs['pk'], self.request.user)
        return redirect('/film/' + str(self.kwargs['pk']))