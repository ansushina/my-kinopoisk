from django.contrib.auth.models import User
from django.db import models


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