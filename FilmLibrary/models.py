from django.db import models
from django.db.models.fields import related
from django.urls import reverse
from django.contrib.auth.models import User


class Film(models.Model):
    name = models.CharField(max_length=250)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=6)
    country = models.CharField(
        max_length=200, verbose_name="Страна выхода", default="Франция"
    )
    slug = models.SlugField(max_length=250)
    year = models.IntegerField(default=2023)
    rating_counts = models.IntegerField(null=True, default=1233)
    image = models.URLField(blank=True, default=" ")
    actors = models.ManyToManyField("Actor", related_name="films")
    description = models.TextField(default="Нет описания", blank=True)
    length = models.CharField(
        max_length=100, verbose_name="Продолжительность", default="1 час 30 минут"
    )
    acceptable_age = models.IntegerField(verbose_name="Возрастное ограничение")
    budget = models.IntegerField(verbose_name="Бюджет", default=12000000)
    genres = models.ManyToManyField("Genre", verbose_name="Жанры")
    director = models.ForeignKey(
        "Director", related_name="produced_films", on_delete=models.CASCADE, blank=True
    )

    def get_absolute_path(self):
        return reverse("movie_detail", args={self.slug})

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=200)
    career = models.CharField(max_length=200, default="Актер")
    slug = models.SlugField(verbose_name="На английском")
    date_of_birth = models.CharField(
        max_length=100, verbose_name="Дата рождения", default=" "
    )
    age = models.CharField(max_length=200, default=34)
    biography = models.TextField(default=" ")
    zodiac_sign = models.CharField(max_length=200, blank=True)
    url = models.URLField(default=" ")

    def get_absolute_path(self):
        return reverse("actor_detail", args={self.slug})

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=200)
    career = models.CharField(max_length=200, default="Актер")
    slug = models.SlugField(verbose_name="На английском")
    date_of_birth = models.CharField(
        max_length=100, verbose_name="Дата рождения", default=" "
    )
    age = models.CharField(max_length=200, default=34)
    biography = models.TextField(default=" ")
    zodiac_sign = models.CharField(max_length=200, blank=True)
    url = models.URLField(default=" ")

    def get_absolute_path(self):
        return reverse("director_detail", args={self.slug})

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя колекции')
    films = models.ManyToManyField("Film", related_name="collections")


class Review(models.Model):
    name = models.CharField(max_length=200)
    film = models.ForeignKey("Film", related_name="reviews", on_delete=models.CASCADE)
    like_count = models.IntegerField()
    text = models.TextField()
    staff = models.BooleanField(default=False)
    created = models.TimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    review = models.ForeignKey("Review", on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=500)
    created = models.TimeField(auto_now_add=True)
