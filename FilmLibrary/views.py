from pkgutil import ModuleInfo
from django.core.paginator import Paginator
from django.shortcuts import Http404, render, get_object_or_404
from .models import Film, Actor, Director, Collection, Review
from city_cinemas.models import Cinema
from django.http import HttpResponse
from django.db.models import Prefetch
from .utils import get_object_and_prefetch


def with_pagination(queryset, request, by_page=21):
    pages_ahead = 4
    pages_before = 3
    paginator = Paginator(queryset, by_page)
    current = 1
    if request.GET.get("page"):
        current = request.GET.get("page")
    current_page_number = current if current else "1"
    page_obj = paginator.get_page(current)
    next = (
        int(current) + pages_ahead
        if (int(current) + pages_ahead) < paginator.num_pages
        else paginator.num_pages
    )
    current = int(current) - pages_before if (int(current) - pages_before) > 0 else 0
    slicer = str(current) + f":{next}"
    return slicer, current_page_number, page_obj


def list_of_films(request):
    films = (
        Film.objects.prefetch_related(
            Prefetch("actors", queryset=Actor.objects.only("id", "name")),
            Prefetch("director", queryset=Director.objects.only("id", "name")),
        )
        .defer("description", "budget", "acceptable_age", "country")
        .all()
    )
    category = request.GET.get("sort-by")
    genre = request.GET.get("genre")
    if category not in ("rating", "name"):
        category = "-rating"
    category = "-rating" if category == "rating" else category
    if genre and genre.isdigit():
        films = films.filter(genres=genre)
    else:
        films = films.order_by(category, "name")
    sort_by_name = category == "name"
    sort_by_name_url = "&sort-by=name" if sort_by_name else ""
    slicer, current_page_number, page_obj = with_pagination(films, request)
    return render(
        request,
        "FilmLibrary/list_of_films.html",
        {
            "page_obj": page_obj,
            "slicer": slicer,
            "num_page": int(current_page_number),
            "sort_by_name": sort_by_name,
            "sort_by_name_url": sort_by_name_url,
        },
    )


def film_detail(request, movie_slug):
    premiere = Collection.objects.filter(
        name="Премьеры", films__slug=movie_slug
    ).exists()
    if premiere:
        film = get_object_and_prefetch(
            movie_slug,
            "actors",
            "director",
            "genres",
            "schedule_set",
            "schedule_set__cinema",
            model=Film,
            primary_key="slug",
        )
        cinemas = Cinema.objects.filter(movies=film).distinct().values()[:3]
        reviews = film.reviews.all().order_by("-like_count")[:3]
        return render(
            request,
            "FilmLibrary/premiere_film_detail.html",
            {"film": film, "cinemas": cinemas, "reviews": reviews},
        )
    film = get_object_and_prefetch(
        movie_slug,
        "actors",
        "director",
        "genres",
        model=Film,
        primary_key="slug",
    )
    reviews = film.reviews.all().order_by("-like_count")[:3]
    return render(
        request, "FilmLibrary/film_detail.html", {"film": film, "reviews": reviews}
    )


def director_detail(request, director_slug):
    director = get_object_or_404(Director, slug=director_slug)
    films = director.produced_films.only(
        "name", "image", "rating", "director_id", "slug"
    ).all()
    return render(
        request, "FilmLibrary/actor_detail.html", {"actor": director, "films": films}
    )


def actor_detail(request, actor_slug):
    actor = get_object_and_prefetch(actor_slug, "films", model=Actor)
    films = actor.films.all()
    return render(
        request, "FilmLibrary/actor_detail.html", {"actor": actor, "films": films}
    )


def list_of_artist(request):
    actors = Actor.objects.order_by("name")
    slicer, current_page_number, page_obj = with_pagination(
        actors, request, by_page=200
    )
    return render(
        request,
        "FilmLibrary/list_of_actors.html",
        {
            "page_obj": page_obj,
            "slicer": slicer,
            "num_page": int(current_page_number),
            "divide_by": 50,
        },
    )


def film_review(request, movie_slug, review_id):
    film = get_object_and_prefetch(movie_slug, model=Film, only=["reviews"])
    review = film.reviews.prefetch_related("comment_set").get(pk=review_id)
    comments = review.comment_set.all()
    return render(
        request,
        "FilmLibrary/film_review.html",
        {"review": review, "comments": comments},
    )
