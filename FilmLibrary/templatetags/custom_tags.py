import datetime
import random

from django import template

register = template.Library()

@register.simple_tag
def today_date():
    date = datetime.datetime.now()
    year = date.year
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)
    formated_date = f'{year}-{month}-{month}'
    return formated_date
@register.filter
def replace_space(value):
    return value.replace('-', ' ').title()

@register.simple_tag
def random_zodiac_sign(actor):
    zodiac_signs = [
        "Овен",
        "Телец",
        "Близнецы",
        "Рак",
        "Лев",
        "Дева",
        "Весы",
        "Скорпион",
        "Стрелец",
        "Козерог",
        "Водолей",
        "Рыбы"
    ]
    zodiac_sign = random.choice(zodiac_signs)
    if actor.zodiac_sign:
        return actor.zodiac_sign
    actor.zodiac_sign = zodiac_sign
    actor.save()
    return zodiac_sign
@register.filter
def minutes_to_hours_minutes(minutes):
    if minutes == '1 час 30 минут':
        return minutes
    double_dot_format = minutes.split(':')
    if len(double_dot_format) == 2:
        try:
            hours = int(double_dot_format[0])
            remaining_minutes = int(double_dot_format[1])
        except:
            hours = 1
            remaining_minutes = 30
    else:
        minutes = int(minutes)
        hours = minutes // 60
        remaining_minutes = minutes % 60

    hours_str = "час" if hours == 1 or (hours % 10 == 1 and hours % 100 != 11) else "часа" if 2 <= hours <= 4 or (2 <= hours % 10 <= 4 and hours % 100 not in (12, 13, 14)) else "часов"
    minutes_str = "минут" if remaining_minutes == 0 or 5 <= remaining_minutes <= 20 or (5 <= remaining_minutes % 10 <= 9 or remaining_minutes % 10 == 0) else "минуты" if 2 <= remaining_minutes % 10 <= 4 else "минут"

    if hours > 0 and remaining_minutes > 0:
        return f"{hours} {hours_str} {remaining_minutes} {minutes_str}"
    elif hours > 0:
        return f"{hours} {hours_str}"
    elif remaining_minutes > 0:
        return f"{remaining_minutes} {minutes_str}"
    else:
        return "0 минут"

@register.filter
def evaluate_word(value):
    if value % 10 == 1 and value % 100 != 11:
        return f"{value} оценка"
    elif 2 <= value % 10 <= 4 and not (12 <= value % 100 <= 14):
        return f"{value} оценки"
    else:
        return f"{value} оценок"
