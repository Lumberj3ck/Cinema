from django.shortcuts import render
from FilmLibrary import models, views


def premiere(request):
    category = request.GET.get('sort-by')
    if category not in ('rating', 'name'):
        category = '-rating'
    category = '-rating' if category == 'rating' else category
    premiers = models.Collection.objects.get(name='Премьеры').films.order_by(category)
    sort_by_name = category == 'name'
    slicer, current_page_number, page_obj = views.with_pagination(premiers, request, by_page=21)
    return render(request, 'FilmLibrary/film_premieres.html',
                  {'page_obj': page_obj,
                   'slicer': slicer,
                   'num_page': int(current_page_number),
                   'sort_by_name':  sort_by_name,
                   })
