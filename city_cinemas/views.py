from django.shortcuts import render, get_object_or_404
from .models import *

def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'city_cinemas/cinema_list.html', {'cinemas': cinemas})


def cinema_detail(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    movie_list_without_dubl = set(cinema.movies.all())
    return render(request, 'city_cinemas/detail_cinema.html', {'cinema': cinema, 'movie_list': movie_list_without_dubl})