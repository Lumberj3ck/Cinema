from django.contrib import admin
from .models import Film, Actor, Director, Genre


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ['name', ]}


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'slug']
    prepopulated_fields = {'slug': ['name', ]}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'upper_case_name']
    prepopulated_fields = {'slug': ['name',]}

    @admin.display(description="Films")
    def upper_case_name(self, obj):
        return f"{obj.films.all()}"

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
