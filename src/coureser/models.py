from coureser.managers import FilmManager, ProfileManager, LikeManager
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Genre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    firstName = models.TextField()
    lastName = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstName + " " + self.lastName


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


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )
    film = models.ForeignKey(
        to=Film,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text + " from " + self.author.user.username + " on " + self.film.title
