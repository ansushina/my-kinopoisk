from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

from coureser.managers.ProfileManger import ProfileManager


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    avatar = models.ImageField(
        upload_to='avatars/%Y/%m/%d/', null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username