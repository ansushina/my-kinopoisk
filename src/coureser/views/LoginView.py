from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic import FormView

from coureser.common.constants import error_no_user
from coureser.forms.LoginForm import LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            return redirect('/')
        cdata = form.cleaned_data
        user = auth.authenticate(**cdata)
        if user is not None:
            auth.login(self.request, user)
            return redirect('/')
        form.add_error(None, error_no_user)
        return self.render_to_response(self.get_context_data(form=form))