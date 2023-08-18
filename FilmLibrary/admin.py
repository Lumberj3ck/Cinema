from django.contrib import admin
from .models import *


@admin.register(Collection)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }
    search_fields = ["name", "age"]


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "slug"]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }
    search_fields = ["name", "id", "slug"]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "upper_case_name"]
    prepopulated_fields = {
        "slug": [
            "name",
        ]
    }
    search_fields = ["name", "age"]

    @admin.display(description="Films")
    def upper_case_name(self, obj):
        return f"{obj.films.all()}"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name"]
