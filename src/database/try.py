from django.core.files.images import ImageFile

from coureser.models import Film
import requests
from django.db.models import ImageField

r = requests.get('https://www.kinopoisk.ru/images/film_big/435.jpg')
Film.objects.create(
    title='title',
    year=1111,
    desription='description',
    image=ImageFile(r.content)
)