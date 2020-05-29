from django.contrib.auth.models import User
from django.db import models

from coureser.managers.LikeManager import LikeManager
from coureser.models.Film import Film
from coureser.models.Profile import Profile


class Like(models.Model):
    film = models.ForeignKey(
        to=Film,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )

    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = LikeManager()

    def __str__(self):
        return "from " + self.author.user.username + " on " + self.film.title