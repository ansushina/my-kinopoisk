from django.contrib import auth
from django.contrib.auth.models import User

from coureser.models.Profile import Profile

from coureser.common.constants import *


class ProfileLogic:
    @staticmethod
    def create_user(data, request):
        if data['password'] != data['rep_password']:
            return error_incorrect_passwords
        user = User.objects.filter(email=data['email'])
        if user:
            return error_invalid_email
        user = User.objects.filter(username=data['username'])
        if user:
            return error_invalid_name

        u = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'])

        p = Profile.objects.create(user=u)
        p.save()
        u.save()

        user = auth.authenticate(**data)
        if user is not None:
            auth.login(request, user)
            return None
        return error_undefined
