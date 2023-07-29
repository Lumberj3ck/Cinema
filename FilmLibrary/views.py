from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Film, Actor, Director


def with_pagination(queryset, request, by_page=20):
    pages_ahead = 4
    pages_before = 3
    paginator = Paginator(queryset, by_page)
    current = 1
    if request.GET.get('page'):
        current = request.GET.get('page')
    current_page_number = current if current else '1'
    page_obj = paginator.get_page(current)
    next = int(current) + pages_ahead if (int(current) + pages_ahead) < paginator.num_pages else paginator.num_pages
    current = int(current) - pages_before if (int(current) - pages_before) > 0 else 0
    slicer = str(current) + f':{next}'
    return slicer, current_page_number, page_obj


# def list_of_films(request):
#     films = Film.objects.all()
#     pages_ahead = 4
#     pages_before = 3
#     paginator = Paginator(films, 20)
#     current = 1
#     if request.GET.get('page'):
#         current = request.GET.get('page')
#     numpage = current if current else '1'
#     page_obj = paginator.get_page(current)
#     next = int(current) + pages_ahead if (int(current) + pages_ahead) < paginator.num_pages else paginator.num_pages
#     current = int(current) - pages_before if (int(current) - pages_before) > 0 else 0
#     return render(request, 'FilmLibrary/list_of_films.html',
#                   {'page_obj': page_obj,
#                    'slicer': str(current) + f':{next}',
#                    'num_page': int(numpage),
#                    })


def list_of_films(request):
    films = Film.objects.all()
    slicer, current_page_number, page_obj = with_pagination(films, request)
    return render(request, 'FilmLibrary/list_of_films.html',
                      {'page_obj': page_obj,
                       'slicer': slicer,
                       'num_page': int(current_page_number),
                       })


def film_detail(request, movie_slug):
    film = get_object_or_404(Film, slug=movie_slug)
    return render(request, 'FilmLibrary/film_detail.html', {'film': film})


def director_detail(request, director_slug):
    director = get_object_or_404(Director, slug=director_slug)
    return render(request, 'FilmLibrary/actor_detail.html', {'actor': director})


def actor_detail(request, actor_slug):
    actor = get_object_or_404(Actor, slug=actor_slug)
    return render(request, 'FilmLibrary/actor_detail.html', {'actor': actor})


# def list_of_artist(request):
#     actors = Actor.objects.order_by('name')
#     pages_ahead = 4
#     pages_before = 3
#     paginator = Paginator(actors, 200)
#     current = request.GET.get('page')
#     numpage = current if current else '1'
#     page_obj = paginator.get_page(current)
#     next = int(current) + pages_ahead if (int(current) + pages_ahead) < paginator.num_pages else paginator.num_pages
#     current = int(current) - pages_before if (int(current) - pages_before) > 0 else 0
#     return render(request, 'FilmLibrary/list_of_actors.html',
#                   {'page_obj': page_obj,
#                    'slicer': str(current) + f':{next}',
#                    'num_page': int(numpage),
#                    'divide_by': 50,
#                    })
def list_of_artist(request):
    actors = Actor.objects.order_by('name')
    slicer, current_page_number, page_obj = with_pagination(actors, request, by_page=200)
    return render(request, 'FilmLibrary/list_of_actors.html',
                  {'page_obj': page_obj,
                   'slicer': slicer,
                   'num_page': int(current_page_number),
                   'divide_by': 50,
                   })
