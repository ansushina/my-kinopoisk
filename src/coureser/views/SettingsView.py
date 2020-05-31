from coureser.forms.SettingsForm import SettingsForm
from coureser.models.Profile import Profile
from django.shortcuts import redirect
from django.views.generic import FormView


class SettingsView(FormView):
    form_class = SettingsForm
    template_name = 'settings.html'

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return redirect('/login/')
        form = SettingsForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            Profile.objects.update(self.request.user, form.cleaned_data)
            return redirect('/')
        return self.render_to_response(self.get_context_data(form=form))
