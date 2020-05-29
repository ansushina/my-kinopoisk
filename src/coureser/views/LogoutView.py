from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')