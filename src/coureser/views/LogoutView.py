from django.contrib import auth
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('/')
