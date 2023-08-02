from django.contrib import admin
from .models import Cinema, Schedule


@admin.register(Cinema)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'address']

@admin.register(Schedule)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['cinema', 'film', 'time']



