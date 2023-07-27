from django.db import models
from django.urls import reverse

class Film(models.Model):
    name = models.CharField(max_length=250)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    slug = models.SlugField()
    year = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='images')
    country = models.CharField(max_length=200)
    actors = models.ManyToManyField('Actor', related_name='films')
    description = models.TextField()
    length = models.CharField(max_length=100, verbose_name='Продолжительность')
    acceptable_age = models.IntegerField(verbose_name="Возрастное ограничение")
    budget = models.IntegerField(verbose_name='Бюджет')
    genres = models.ManyToManyField('Genre', verbose_name='Жанры')
    director = models.ForeignKey('Director', related_name='produced_films', on_delete=models.CASCADE)

    def get_absolute_path(self):
        return reverse('movie_detail', args={self.slug})

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name='На английском')
    date_of_birth = models.CharField(max_length=100, verbose_name='Дата рождения')
    age = models.CharField(max_length=200)
    biography = models.TextField()
    zodiac_sign = models.CharField(max_length=200, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    career = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name='На английском')
    date_of_birth = models.CharField(max_length=100, verbose_name='Дата рождения')
    age = models.CharField(max_length=200)
    biography = models.TextField()
    zodiac_sign = models.CharField(max_length=200, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
