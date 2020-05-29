from django.db import models
from django.http import JsonResponse


class LikeManager(models.Manager):
    def like(self, value, film_id, user):
        print(film_id)
        film = self.filter(id=film_id).first()
        like = self.filter(author=user.profile, film_id=film_id).first()
        if like:
            setattr(like, 'value', value)
            like.save()
            return JsonResponse({"status": "ok"})
        self.create(author=user.profile, film_id=film_id, value=value)
        return JsonResponse({"status": "ok"})