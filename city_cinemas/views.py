import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import SearchForm
from .models import *
from django.contrib.postgres.search import TrigramSimilarity
from FilmLibrary.models import *
from FilmLibrary.utils import get_object_and_prefetch
from django.db.models import Prefetch


def cinema_list(request):
    cinemas = Cinema.objects.defer("description", "longitude", "lattitude").all()
    return render(request, "city_cinemas/cinema_list.html", {"cinemas": cinemas})


def cinema_detail(request, cinema_id):
    # cinema = get_object_or_404(Cinema, id=cinema_id)
    cinema = get_object_and_prefetch(
        cinema_id,
        "movies",
        "schedule_set",
        "schedule_set__film",
        model=Cinema,
        primary_key="id",
    )
    movie_list_without_dubl = cinema.movies.prefetch_related("genres").all().distinct()
    return render(
        request,
        "city_cinemas/detail_cinema.html",
        {"cinema": cinema, "movie_list": movie_list_without_dubl},
    )


def session_detail(request, movie_slug, session_id):
    movie_session = get_object_and_prefetch(
        session_id,
        Prefetch("film", queryset=Film.objects.only("name")),
        Prefetch("cinema", queryset=Cinema.objects.only("name")),
        model=Schedule,
        primary_key="id",
    )
    seats = movie_session.selected_seats.order_by("row_num", "seat_num")
    referer = request.META.get("HTTP_REFERER")
    reserved_seats = json.dumps(list(seats.values()))
    return render(
        request,
        "city_cinemas/session_detail.html",
        {
            "movie_session": movie_session,
            "reserved_seats": reserved_seats,
            "referer": referer,
        },
    )


def search(request):
    form = SearchForm(request.POST)
    if form.is_valid():
        query = form.cleaned_data.get("query")
        actors = (
            Actor.objects.annotate(similarity=TrigramSimilarity("name", query))
            .filter(similarity__gt=0.3)
            .order_by("-similarity")[:5]
        )
        directors = (
            Director.objects.annotate(similarity=TrigramSimilarity("name", query))
            .filter(similarity__gt=0.3)
            .order_by("-similarity")[:5]
        )
        films = (
            Film.objects.annotate(similarity=TrigramSimilarity("name", query))
            .filter(similarity__gt=0.3)
            .order_by("-similarity")[:5]
        )
        empty = not any((actors, directors, films))
        return render(
            request,
            "city_cinemas/search_results.html",
            {
                "actors": actors,
                "films": films,
                "directors": directors,
                "empty": empty,
                "query": query,
            },
        )
    return render(request, "city_cinemas/search_results.html", {"empty": True})
