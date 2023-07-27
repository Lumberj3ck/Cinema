from django.shortcuts import render, get_object_or_404
from .models import Film, Actor


def list_of_films(request):
    films = Film.objects.all()
    return render(request, 'FilmLibrary/list_of_films.html', {'films': films})

def film_detail(request, movie_slug):
    film = get_object_or_404(Film, slug=movie_slug)
    return render(request, 'FilmLibrary/film_detail.html', {'film': film})

def director_detail(request, director_slug):
    pass

def actor_detail(request, actor_slug):
    actor = get_object_or_404(Actor, slug=actor_slug)
    return render(request, 'FilmLibrary/actor_detail.html', {'actor': actor})
