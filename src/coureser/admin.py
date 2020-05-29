from django.contrib import admin


# Register your models here.
from coureser.models.Actor import Actor
from coureser.models.Comment import Comment
from coureser.models.Country import Country
from coureser.models.Film import Film
from coureser.models.Genre import Genre
from coureser.models.Like import Like
from coureser.models.Profile import Profile

admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Film)
admin.site.register(Comment)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Country)