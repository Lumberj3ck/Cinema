from django.db import models
from FilmLibrary.models import Film
from django.urls import reverse


class Cinema(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    longitude = models.CharField(max_length=200, default='76.934287')
    lattitude = models.CharField(max_length=200, default='43.233651')
    movies = models.ManyToManyField(Film, through='Schedule')
    address = models.CharField(max_length=200)

    def get_absolute_path(self):
        return reverse('cinema_detail', args={self.id})

    def __str__(self):
        return self.name

class Schedule(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    time = models.TimeField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.film.name} at {self.cinema.name}"
