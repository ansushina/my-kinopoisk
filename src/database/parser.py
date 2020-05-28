import json


class Parser:
    def __init__(self):
        films_data = open('database/films_data.json')
        films = json.load(films_data)
        films_data.close()
        genres = []

        for film in films:
            for g in film['genres']:
                if g not in genres:
                    genres.append(g)

        countries = []
        for film in films:
            for c in film['countries']:
                if c not in countries:
                    countries.append(c)

        persons_data = open('database/persons_data.json')
        persons = json.load(persons_data)
        persons_data.close()

        actors = []
        for person in persons:
            name = person['name'].split()
            if len(name) > 1:
                last = name[1]
            else:
                last = ''
            actors.append({'first_name': name[0], 'last_name': last, 'id': persons.index(person)})

        films_images = open('database/films_data_images.json')

        images = json.load(films_images)

        films_images.close()

        my_films = []

        for film in films:
            year = film['year']
            title = film['title']
            description = film['description']

            film_actors = []
            for id in film['persons_id']:
                film_actors.append(actors[id])
            image = images[films.index(film)]
            my_films.append({'year': year,
                             'title': title,
                             'description': description,
                             'countries': film['countries'],
                             'genres': film['genres'],
                             'actors': film_actors,
                             'image': image})

        self.genres = genres
        self.countries = countries
        self.actors = actors
        self.films = my_films

    def get_films(self):
        return self.films

    def get_actors(self):
        return self.actors

    def get_genres(self):
        return self.genres

    def get_countries(self):
        return self.countries
