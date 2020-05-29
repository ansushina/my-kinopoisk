from django.db import models

from coureser.managers.FilmManager import FilmManager
from coureser.models.Actor import Actor
from coureser.models.Country import Country
from coureser.models.Genre import Genre


class Film(models.Model):
    year = models.IntegerField(default=0)
    title = models.TextField()
    description = models.TextField()
    rating = models.IntegerField(default=0)
    genres = models.ManyToManyField(
        to=Genre,
        blank=True)
    actors = models.ManyToManyField(
        to=Actor,
        blank=True
    )
    countries = models.ManyToManyField(
        to=Country,
        blank=True
    )

    image = models.ImageField(
        upload_to='films/%Y/%m/%d/', null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    objects = FilmManager()

    def __str__(self):
        return self.title

