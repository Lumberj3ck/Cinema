from django.db import models
from FilmLibrary.models import Film
from django.urls import reverse


class Cinema(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    longitude = models.CharField(max_length=200, default='76.934287')
    lattitude = models.CharField(max_length=200, default='43.233651')
    movies = models.ManyToManyField(Film, through='Schedule')
    address = models.CharField(max_length=200)

    def get_absolute_path(self):
        return reverse('cinema_detail', args={self.id})

    def __str__(self):
        return self.name


class Seat(models.Model):
    row_num = models.IntegerField()
    seat_num = models.IntegerField()


    def __str__(self):
        return f'{self.row_num} ряд {self.seat_num} место'

class Schedule(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.TimeField(blank=True, null=True)
    price = models.IntegerField(default=1500)
    selected_seats = models.ManyToManyField('Seat', verbose_name='Занятые места', related_name='session')

    def __str__(self):
        return f"{self.film.name} at {self.cinema.name}"
