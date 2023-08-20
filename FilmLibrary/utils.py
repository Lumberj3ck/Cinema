import os
import django
from django.urls.exceptions import Http404

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cinema.settings")
django.setup()
from FilmLibrary.models import *


def get_object_and_prefetch(
    object_key: str, *args, model=Film, primary_key="slug", **kwargs
):
    only = kwargs.get("only")
    filters = {primary_key: object_key}
    queryset = (
        model.objects.prefetch_related(*args).only(*only if only else "")
    ).filter(**filters)
    if queryset:
        return queryset[0]
    raise Http404("We do not have such film")


if __name__ == "__main__":
    response = get_object_and_prefetch(
        "oppengeimer",
        "actors",
        "director",
        model=Film,
        primary_key="slug",
    )
    print(response)
