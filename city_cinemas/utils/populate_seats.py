import random, django, os
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cinema.settings")
django.setup()
from city_cinemas.models import *

seat_numbers = {7: 17, 8: 18}


def get_exclude_list() -> list:
    exclude_list = []
    quantity_ex_seats = random.randint(60, 65)
    for _ in range(quantity_ex_seats):
        random_row = random.randint(1, 9)
        upper_border = 14
        if random_row in seat_numbers:
            upper_border = seat_numbers[random_row]
        random_seat = random.randint(1, upper_border)
        exclude_list.append((random_row, random_seat))
    return exclude_list


def make_served_seats() -> list:
    exclude_list = get_exclude_list()
    ordered_exclude = sorted(list(set(exclude_list)))
    current_exclude = 0
    served_seats = []
    for row in range(1, 9):
        n = 14
        if row in seat_numbers.keys():
            n = seat_numbers[row]
        for seat in range(1, n+1):
            r = ordered_exclude[current_exclude][0]
            s = ordered_exclude[current_exclude][1]
            # Seat.objects.get_or_create(row_num=row, seat_num=seat)
            if row == r and seat == s and current_exclude <= len(ordered_exclude) - 1:
                current_exclude = current_exclude + 1 if current_exclude != len(ordered_exclude) - 1 else current_exclude
                continue
            served_seats.append((row, seat))
    return served_seats


def populate_seats(create_all_new=True):
    for schedule in Schedule.objects.all():
            if not create_all_new and schedule.selected_seats.all().__len__() <= 1:
                continue
            schedule.selected_seats.all().delete()
            exclude_list = get_exclude_list()
            served_seats = sorted(list(set(exclude_list)))
            print(len(served_seats), len(exclude_list))
            for seat in served_seats:
                seat_object = Seat.objects.get_or_create(row_num=seat[0], seat_num=seat[1])
                schedule.selected_seats.add(seat_object[0])


if __name__ == "__main__":
    start = datetime.now().time()
    populate_seats()
    print(datetime.now().time(), start)
