from django.urls import path
from .views import *

urlpatterns = [
    path('', cinema_list, name='cinema_list'),
    path('<int:cinema_id>', cinema_detail, name='cinema_detail'),
    path('<slug:movie_slug>/<int:session_id>', session_detail, name='session'),
]
