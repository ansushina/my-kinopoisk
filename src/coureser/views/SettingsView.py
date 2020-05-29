from django.shortcuts import redirect
from django.views.generic import FormView

from coureser.forms.SettingsForm import SettingsForm
from coureser.models.Profile import Profile


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