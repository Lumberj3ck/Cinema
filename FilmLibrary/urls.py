from django.urls import path
from FilmLibrary import views


urlpatterns = [
    path("", views.list_of_films, name="all_movies"),
    path("person/", views.list_of_artist, name="all_persons"),
    path("person/<slug:actor_slug>/", views.actor_detail, name="actor_detail"),
    path(
        "<slug:movie_slug>/review/<int:review_id>/",
        views.film_review,
        name="film_review",
    ),
    path("<slug:movie_slug>/", views.film_detail, name="movie_detail"),
    path(
        "director/<slug:director_slug>", views.director_detail, name="director_detail"
    ),
]
