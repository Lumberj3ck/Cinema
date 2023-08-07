import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *


def cinema_list(request):
    cinemas = Cinema.objects.all()
    return render(request, 'city_cinemas/cinema_list.html', {'cinemas': cinemas})


def cinema_detail(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    movie_list_without_dubl = set(cinema.movies.all())
    return render(request, 'city_cinemas/detail_cinema.html', {'cinema': cinema, 'movie_list': movie_list_without_dubl})


def session_detail(request, movie_slug, session_id):
    movie_session = Schedule.objects.get(id=session_id)
    seats = movie_session.selected_seats.order_by('row_num', 'seat_num')
    referer = request.META.get('HTTP_REFERER')
    reserved_seats = json.dumps(list(seats.values()))
    return render(request, 'city_cinemas/session_detail.html', {'movie_session': movie_session, 'reserved_seats': reserved_seats, 'referer': referer})
