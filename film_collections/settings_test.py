from django.test import *
from FilmLibrary.models import *

class Settings(TestCase):
    @classmethod
    def setUpClass(cls):
        TestCase.setUpClass()
        cls.premiere_collection = Collection.objects.create(name="Премьеры")
        user = User.objects.create_user(username="testuser", password="password123")
        user.email = "test@example.com"
        user.first_name = "Test"
        user.last_name = "User"
        user.save()
        cls.user = user
        actor1 = Actor.objects.create(
            name="Actor 1",
            career="Актер",
            slug="actor-1",
            age="30",
            biography="Биография актера 1",
        )
        actor2 = Actor.objects.create(
            name="Actor 2",
            career="Актер",
            slug="actor-2",
            age="25",
            biography="Биография актера 2",
        )
        director = Director.objects.create(
            name="Director 1",
            career="Режиссер",
            slug="director-1",
            age="40",
            biography="Биография режиссера 1",
        )
        genre1 = Genre.objects.create(name="Жанр 1")
        genre2 = Genre.objects.create(name="Жанр 2")
        cls.film = Film.objects.create(
            name="My Film",
            rating=7.5,
            country="USA",
            slug="my-film",
            year=2023,
            rating_counts=1500,
            image="https://example.com/image.jpg",
            description="Описание фильма",
            length="120",
            acceptable_age=16,
            budget=10000000,
            director=director,
        )
        cls.film1 = Film.objects.create(
            name="Film 1",
            rating=7.5,
            country="USA",
            slug="my-film1",
            year=20222,
            rating_counts=1500,
            image="https://example.com/image.jpg",
            description="Описание фильма",
            length="120",
            acceptable_age=16,
            budget=10000000,
            director=director,
        )
        cls.film.actors.add(actor1, actor2)
        cls.film.genres.add(genre1, genre2) 
        cls.film1.actors.add(actor1, actor2)
        cls.film1.genres.add(genre1, genre2) 
        cls.premiere_collection.films.add(cls.film, cls.film1)

