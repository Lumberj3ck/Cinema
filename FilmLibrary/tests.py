from django.test import TestCase, client
from django.urls import resolve
from FilmLibrary import views
from django.contrib.auth.models import User
from .models import *


class HomePage(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="password123")
        user.email = "test@example.com"
        user.first_name = "Test"
        user.last_name = "User"
        user.save()
        self.user = user
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
        self.film = Film.objects.create(
            name="My Film",
            rating=7.5,
            country="USA",
            slug="my-film",
            year=2023,
            rating_counts=1500,
            image="https://example.com/image.jpg",
            description="Описание фильма",
            length="2 часа",
            acceptable_age=16,
            budget=10000000,
            director=director,
        )

        self.film.actors.add(actor1, actor2)
        self.film.genres.add(genre1, genre2)

    def setup_review(self):
        review = Review.objects.create(
            name="Some film Name review",
            like_count=5,
            film=self.film,
            text="Good or bad film clients opinion",
            staff=True,
        )
        comment = Comment.objects.create(
            user=self.user, review=review, text="i like it"
        )

    def test_review_db(self):
        # Also review model should have time stamp created and last saved
        self.setup_review()
        com_count = Comment.objects.all().count()
        self.assertEqual(com_count, 1)

    def test_review_url(self):
        self.setup_review()
        response = self.client.get("http://127.0.0.1:8000/movies/my-film/review")
        # print(response.func)
        # self.assertEqual(response.func, views.film_review)

    def test_review_template(self):
        self.setup_review()
        response = self.client.get("http://127.0.0.1:8000/movies/my-film/review")
        html = response.content.decode()
        self.assertTemplateUsed(response, "FilmLibrary/film_review.html")
        self.assertIn("<title>Some film Name review</title>", html)
        self.assertIn(
            "<div class='coments'><div class='comment'>i like it</div></div>", html
        )
