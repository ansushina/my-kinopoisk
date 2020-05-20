from django.contrib import admin

from coureser import models

# Register your models here.
admin.site.register(models.Profile)
admin.site.register(models.Like)
admin.site.register(models.Film)
admin.site.register(models.Comment)
admin.site.register(models.Actor)
admin.site.register(models.Genre)
admin.site.register(models.Country)