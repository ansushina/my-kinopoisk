from django.contrib import auth
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        auth.logout(request)
        return redirect('/')
