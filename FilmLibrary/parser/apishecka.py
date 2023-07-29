import json
import re

from slugify import slugify

import requests
import os
import django
import json
from datetime import datetime
import locale

desired_language = 'ru_RU'
locale.setlocale(locale.LC_TIME, (desired_language, 'UTF-8'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'Cinema.settings')
django.setup()

from FilmLibrary.models import Genre, Film, Director, Actor

headers = {
    'X-API-KEY': 'db9ef8a6-17f1-45b1-b580-312342cfafbc',
    'Content-Type': 'application/json',
}


def get_url(url):
    response = requests.get(f'https://kinopoiskapiunofficial.tech/{url}',
                            headers=headers)
    return response.text


def get_staff(id):
    staff = json.loads(get_url(f'/api/v1/staff?filmId={id}'))
    first = True
    actors = []
    director = None
    for staff in staff[:6]:
        if staff['professionKey'] == 'DIRECTOR':
            model = Director
            director = get_obj_or_create(model, staff)
            first = False
        elif staff['professionKey'] == 'ACTOR':
            model = Actor
            actor = get_obj_or_create(model, staff)
            actors.append(actor)
    if not director:
        director = Director.objects.get(pk=535)
    return director, actors


def get_object_or_none(model, param, value):
    try:
        object = model.objects.get(param=value)
        return object
    except Genre.DoesNotExist:
        return None


def get_obj_or_create(model, staff):
    try:
        return model.objects.get(name=staff['nameRu'])
    except:
        actor_detail = json.loads(get_url(f"/api/v1/staff/{staff['staffId']}"))
        try:
            biography = actor_detail['facts'][0] if actor_detail['facts'] else ' '
        except:
            biography = '  '
        date_string = actor_detail['birthday']
        if date_string is not None:
            date_obj = datetime.strptime(date_string, "%Y-%m-%d")
            birthday = date_obj.strftime("%d %B %Y")
        birthday = ''
        career = actor_detail['profession'] if actor_detail['profession'] else 'Актёр'
        return model.objects.create(name=staff["nameRu"],
                                    age=actor_detail["age"],
                                    slug=slugify(staff['nameRu']),
                                    date_of_birth=birthday,
                                    biography=biography,
                                    career=career,
                                    url=actor_detail['posterUrl'],
                                    )


def main_parser(page=1):
    season_premieres = get_url(f'api/v2.2/films/top?type=TOP_100_POPULAR_FILMS&page={page}')
    # season_premieres = get_url('api/v2.2/films/premieres?year=2023&month=JULY')
    js = json.loads(season_premieres)
    print(season_premieres)
    for film in js['films']:
        id = film['filmId']
        name = film['nameRu']
        year = film['year']
        image = film['posterUrl']
        country = film['countries'][0]['country']
        length = film['filmLength']
        if not length:
            length = '1 час 30 минут'
        try:
            budget = json.loads(get_url(f'api/v2.2/films/{id}/box_office'))['items'][0]['amount']
        except Exception as e:
            print(e)
            budget = 120_000_000
        film_information = json.loads(get_url(f'api/v2.2/films/{id}'))
        rating = film_information.get('ratingImdb')
        rating = rating if rating else 6
        description = film_information['description'] if film_information['description'] else 'Нет описания'
        rating_counts = film_information['ratingImdbVoteCount']
        rating_counts = rating_counts if rating_counts else 1000
        text_with_age = film_information['ratingAgeLimits']
        if text_with_age:
            matches = re.findall(r'\d+', text_with_age)
            acceptable_age = matches[0] if matches else 12
        acceptable_age = 12
        slug = slugify(name)
        genres = [Genre.objects.get_or_create(name=genre['genre'])[0] for genre in film['genres']]
        director, actors = get_staff(id)
        film_obj = Film.objects.create(name=name, year=year, image=image, country=country,
                                       rating=rating,
                                       rating_counts=rating_counts,
                                       acceptable_age=acceptable_age,
                                       slug=slug,
                                       length=length,
                                       budget=budget,
                                       director=director,
                                       description=description
                                       )
        film_obj.genres.add(*genres)
        film_obj.actors.add(*actors)
        print(name, director, actors)


if __name__ == '__main__':
    # for i in range(6, 36):
    #     main_parser(i)
    s = get_url('/api/v2.1/films/search-by-keyword?keyword=Басқа Вариант Жоқ')
    print(s)