from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views.generic import FormView

from coureser.common.constants import *
from coureser.forms.RegisterForm import RegisterForm
from coureser.logic.ProfileLogic import ProfileLogic


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('/')  # todo равильные редиректы

        error = ProfileLogic.create_user(form.cleaned_data, self.request)
        if not error:
            return redirect('/')
        elif error == error_invalid_email:
            form.add_error('email', ValidationError(error, code='invalid'))
        elif error == error_incorrect_passwords:
            form.add_error('password', ValidationError(error, code='invalid'))
            form.add_error('rep_password', ValidationError(error, code='invalid'))
        elif error == error_invalid_name:
            form.add_error('username', ValidationError(error, code='invalid'))
        return self.render_to_response(self.get_context_data(form=form))
