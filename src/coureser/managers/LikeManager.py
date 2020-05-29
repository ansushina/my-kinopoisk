from django.db import models
from django.http import JsonResponse


class LikeManager(models.Manager):
    def like(self, value, film_id, user):
        print(film_id)
        film = self.filter(id=film_id).first()
        like = self.filter(author_id=user.id, film_id=film_id).first()
        if like:
            setattr(like, 'value', value)
            like.save()
            return JsonResponse({"status": "ok"})
        print(user.id)
        self.create(author_id=user.id, film_id=film_id, value=value)
        return JsonResponse({"status": "ok"})