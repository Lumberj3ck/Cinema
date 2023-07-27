import random

from django import template

register = template.Library()

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