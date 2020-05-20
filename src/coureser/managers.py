from django.db import models
from django.db.models import Count


class FilmManager(models.Manager):
    def new_top(self):
        return self.order_by('-created_at')[:10]

    def most_commented(self):
        return self.annotate(count=Count('comment')).order_by('-count')[:10]
