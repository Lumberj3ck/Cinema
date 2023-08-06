from django.contrib import admin
from .models import Cinema, Schedule, Seat


@admin.register(Cinema)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'address']

@admin.register(Schedule)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['cinema', 'film', 'time']

@admin.register(Seat)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ('row_num', 'seat_num')



