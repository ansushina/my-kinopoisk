from django.contrib import auth
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.views.generic import FormView

from coureser.forms.RegisterForm import RegisterForm
from coureser.models.Profile import Profile


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
