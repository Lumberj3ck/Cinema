# populate_db.py
import os
import django
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cinema.settings")
django.setup()
from FilmLibrary.models import Actor, Director

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

if __name__ == "__main__":
    pass
