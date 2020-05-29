import os

import requests
from coureser.models import *
from database.parser import Parser
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand
from django.db import transaction

parser = Parser();


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    @transaction.atomic()
    def handle(self, *args, **options):

        self.generate_genres()
        self.generate_countries()
        self.generate_actors()
        self.generate_films()
        self.set_images()

    def generate_genres(self):
        genres = parser.get_genres()
        print("GENERATE_GENRES ", len(genres))
        for g in genres:
            Genre.objects.create(
                name=g,
            )

    def generate_countries(self):
        countries = parser.get_countries()
        print("GENERATE_COUNTRIES ", len(countries))
        for c in countries:
            Country.objects.create(
                name=c,
            )

    def generate_actors(self):
        actors = parser.get_actors()
        print("GENERATE_ACTORS ", len(actors))
        for actor in actors:
            Actor.objects.create(
                firstName=actor['first_name'],
                lastName=actor['last_name'],
            )

    def generate_films(self):
        films = parser.get_films()
        print("GENERATE_FILMS ", len(films))
        genres = Genre.objects.all()
        genres_id = list(Genre.objects.values_list('id', flat=True))
        actors = Actor.objects.all()
        countries = Country.objects.all()
        for film in films:
            f = Film.objects.create(
                title=film['title'],
                year=film['year'],
                description=film['description']
            )
            f.save()
            for g in film['genres']:
                for genre in genres:
                    if genre.name == g:
                        f.genres.add(genre.id)
            for g in film['actors']:
                for actor in actors:
                    if actor.firstName == g['first_name'] and actor.lastName == g['last_name']:
                        f.actors.add(actor.id)
            for g in film['countries']:
                for country in countries:
                    if country.name == g:
                        f.countries.add(country.id)
            print(films.index(film))

    def set_images(self):
        films = parser.get_films()
        for film in films:
            r = requests.get(film['image'])
            film_ob = Film.objects.filter(title=film['title']).first()

            name = film['image'].split('/')[5]
            print(name)
            f = open(name, "wb+")
            f.write(r.content)

            djangofile = ImageFile(f)
            film_ob.image.save('new', djangofile)
            f.close()

            os.remove(name)
