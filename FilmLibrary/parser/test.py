headers = {
    'X-API-KEY': 'db9ef8a6-17f1-45b1-b580-312342cfafbc',
    'Content-Type': 'application/json',
}
import requests
from apishecka import Director


def get_url(url):
    response = requests.get(f'https://kinopoiskapiunofficial.tech/{url}',
                            headers=headers)
    return response.text


# print(get_url('api/v2.2/films/top?type=TOP_100_POPULAR_FILMS&page=3'))
dubl = []
# for director in Director.objects.all():
#     Director.objects.filter(pk__in=Director.objects.filter(name=director.name).values_list('id', flat=True)[1:]).delete()
for cinema in Cinema.objects.all():
    query = Director.objects.filter(slug=director.slug).values_list('id', flat=True)
    if query.count() > 1:
        dubl.append(query)
print(len(dubl), dubl)