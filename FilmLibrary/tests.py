from django.test import TestCase, client
from django.urls import resolve, reverse
from FilmLibrary import views
from .views import *
from django.contrib.auth.models import User
from .models import *
from film_collections.settings_test import Settings

class HomePage(Settings):
    def setup_review(self):
        for i in range(5):
            review = Review.objects.create(
                name="Some film Name review",
                like_count=i,
                film=self.film,
                text="Good or bad film clients opinion",
                staff=True,
            )
            comment = Comment.objects.create(
                username='Lumberjack', review=review, text="i like it"
            )

    def test_review_link_in_film_detail(self):
        self.setup_review()
        response = self.client.get("/movies/my-film/")
        film = Film.objects.get(slug="my-film")
        reviews = film.reviews.all().order_by("-like_count")
        link_counter = 0
        for review in reviews:
            review_link = reverse(
                "film_review",
                kwargs={"movie_slug": self.film.slug, "review_id": review.id},
            )
            if link_counter > 2:
                self.assertNotContains(
                    response, f"<a href='{review_link}'>{review.text}</a>"
                )
                continue
            link_counter += 1
            self.assertContains(response, f"<a href='{review_link}'>{review.text}</a>")

    def test_review_link_in_premiere_film_detail(self):
        self.setup_review()
        film = Film.objects.get(slug="my-film")
        self.premiere_collection.films.add(film)
        reviews = film.reviews.all().order_by("-like_count")
        response = self.client.get("/movies/my-film/")
        link_counter = 0
        for review in reviews:
            review_link = reverse(
                "film_review",
                kwargs={"movie_slug": self.film.slug, "review_id": review.id},
            )
            if link_counter > 2:
                self.assertNotContains(
                    response, f"<a href='{review_link}'>{review.text}</a>"
                )
                continue
            link_counter += 1
            self.assertContains(response, f"<a href='{review_link}'>{review.text}</a>")

    def test_review_url(self):
        self.setup_review()
        review = self.film.reviews.all()[0]
        url = reverse(
            "film_review", kwargs={"movie_slug": self.film.slug, "review_id": review.id}
        )
        view_func = self.client.get(url).resolver_match.func
        self.assertEqual(view_func, views.film_review)

    def test_review_db(self):
        self.setup_review()
        com_count = Comment.objects.all().count()
        self.assertEqual(com_count, 5)

    def test_film_detail_url(self):
        self.setup_review()
        view = resolve("/movies/my-film/")
        self.assertEqual(view.func, film_detail)

    def test_review_template(self):
        self.setup_review()
        review = self.film.reviews.all()[0]
        response = self.client.get(
            f"http://127.0.0.1:8000/movies/my-film/review/{review.id}/"
        )
        comment_text = Review.objects.all()[0].comment_set.all()[0].text
        self.assertTemplateUsed(response, "FilmLibrary/film_review.html")
        self.assertContains(response, "<title>Some film Name review</title>")
        self.assertContains(response, f"<div class='comment'>{comment_text}</div>")

    def test_review_text(self):
        self.setup_review()
        review = self.film.reviews.all()[0]
        response = self.client.get(
            f"http://127.0.0.1:8000/movies/my-film/review/{review.id}/"
        )
        review_text = review.text
        self.assertContains(response, f"<div class='review_text'>{review_text}</div>")

    def test_review_likes_count(self):
        self.setup_review()
        review = self.film.reviews.all()[0]
        response = self.client.get(
            f"http://127.0.0.1:8000/movies/my-film/review/{review.id}/"
        )
        likes_count = review.like_count
        self.assertContains(response, f"<div class='likes_counter'>{likes_count}</div>")

    ## ADD MARKDOWN INTO ADMIN REVIEW EDITOR
