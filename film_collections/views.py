from django.shortcuts import render
from FilmLibrary import models, views
from django.db.models import Prefetch


def premiere(request):
    category = request.GET.get("sort-by")
    genre = request.GET.get("genre")
    if category not in ("rating", "name"):
        category = "-rating"
    premiers = (
        models.Collection.objects.get(name="Премьеры")
        .films.prefetch_related(
        Prefetch("actors", queryset=models.Actor.objects.only("id", "name")),
        Prefetch(
                    "director", queryset=models.Director.objects.only("id", "name")
                ),
            )
            .defer("description", "budget", "acceptable_age", "country")
    ).order_by(category)
    if genre and genre.isdigit():
        premiers = premiers.filter(genres=genre)
    sort_by_name = category == "name"
    if len(premiers) > 21:
        slicer, current_page_number, page_obj = views.with_pagination(
            premiers, request, by_page=21
        )
    else:
        slicer, current_page_number, page_obj = 2, 1, premiers
    return render(
        request,
        "FilmLibrary/film_premieres.html",
        {
            "page_obj": page_obj,
            "slicer": slicer,
            "num_page": int(current_page_number),
            "sort_by_name": sort_by_name,
        },
    )
