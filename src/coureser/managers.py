from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Q
from django.http import JsonResponse


class FilmManager(models.Manager):
    def new_top(self):
        return self.order_by('-created_at')[:10]

    def most_commented(self):
        return self.annotate(count=Count('comment')).order_by('-count')[:10]

    def most_rating(self):
        return self.order_by('rating')[:10]

    def count_rating(self, film_id):
        film = self.get(id=film_id)
        likes = film.like_set.all()
        sum = 0
        for like in likes:
            sum += like.value
        if len(likes) != 0:
            rating = sum / len(likes)
            setattr(film, 'rating', rating)
            film.save(update_fields=['rating'])

    def search_with_filters(self, querydict):
        films = self.all()
        params = ['q', 'genre', 'country', 'actor', 'year_from', 'year_to']
        for p in params:
            item = querydict.getlist(p)
            if len(item) == 1:
                if p == 'q' and item[0] != '':
                    films = films.filter(
                        Q(title__icontains=item[0])
                    )
                if p == 'year_from' and item[0] != '':
                    films = films.filter(year__gte=item[0])
                elif p == 'year_to' and item[0] != '':
                    films = films.filter(year__lte=item[0])
            if len(item) >= 1:
                if p == 'genre':
                    films = films.filter(genres__id__in=item)
                elif p == 'country':
                    films = films.filter(countries__id__in=item)
                elif p == 'actor':
                    films = films.filter(actors__id__in=item)
        return films


class ProfileManager(models.Manager):
    def update(self, user, cdata):
        user_fields, profile_fields = ['username', 'email'], ['avatar']
        fields_to_update = {'user': [], 'profile': []}
        profile = self.get(user=user.id)
        user = User.objects.get(pk=user.id)
        for key in user_fields:
            value = cdata.get(key, False)
            if value:
                fields_to_update['user'].append(key)
                setattr(user, key, value)

        value = cdata.get('avatar', False)
        if value:
            fields_to_update['profile'].append('avatar')
            print(value)
            setattr(profile, 'avatar', value)
        user.save(update_fields=fields_to_update['user'])
        profile.save(update_fields=fields_to_update['profile'])


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
