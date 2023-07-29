# populate_db.py
import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cinema.settings")
django.setup()
from FilmLibrary.models import Actor, Director, Film, Collection

with open('actors.txt', 'r') as file:
    text = file.read()


# some_data = json.loads(text)
def save(some_data: dict):
    for value in some_data.values():
        model = Director if value['model'] == 'Director' else Actor
        model.objects.create(name=value["name"],
                             age=value["age"],
                             slug=value['slug'],
                             date_of_birth=value['date_of_birth'],
                             biography=value['biography'],
                             career=value['career'],
                             url=value['image_url'],
                             )


def update_collections(name):
    try:
        film = Film.objects.get(name=name)
    except:
        print('We do not have that film', name)
        return
    premieres = Collection.objects.get(id=1)
    premieres.films.add(film)
    print('Success')


if __name__ == "__main__":
    names = ['Астрал 5. Красная дверь', 'Барби', 'Басқа Вариант Жоқ', 'Бесконечная свадьба', 'Жанна Дюбарри',
             'Индиана Джонс и колесо судьбы', 'Кентавр', 'Коронный бросок. Фильм', 'Кошмар', 'Круче некуда',
             'Кукла. Реинкарнация зла', 'Любой проблема шешемiз', 'Миссия: невыполнима. Смертельная расплата. Часть 1',
             'Оппенгеймер', 'Особняк с привидениями', 'Схватка с дьяволом', 'Чарли и фантастическая четверка',
             'Человек-Паук: Паутина Вселенных']
    # for film in names:
    update_collections('Басқа Вариант Жоқ')
