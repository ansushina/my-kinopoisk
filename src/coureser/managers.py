
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class FilmManager(models.Manager):
    def new_top(self):
        return self.order_by('-created_at')[:10]

    def most_commented(self):
        return self.annotate(count=Count('comment')).order_by('-count')[:10]


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
            setattr(profile, 'avatar', value)
        user.save(update_fields=fields_to_update['user'])
        profile.save(update_fields=fields_to_update['profile'])
