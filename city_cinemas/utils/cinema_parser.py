from django.utils.text import slugify
from requests import request
from bs4 import BeautifulSoup
import random, json, os, django, re
from populate_seats import populate_seats
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cinema.settings")
django.setup()
from FilmLibrary.models import Film
from city_cinemas.models import *
from slugify import slugify

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/95.0.1020.30 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
]

headers = {
    'User-Agent': random.choice(user_agents),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Connection': 'Connection',
    'Cookie': 'ka_city=YWxtYXR5Lmtpbm9hZmlzaGEuaW5mb3xhbG1hdHk%3D; _ga_3GNTWFZ027=GS1.1.1690303731.6.0.1690303731.60.0.0; _ga=GA1.2.1818900436.1690194461; _gid=GA1.2.1522577555.1690194462; chash=VdeaQJ8M1U; _ga_YXMWP5QFFQ=GS1.1.1690200932.1.0.1690200932.0.0.0; PHPSESSID=268e022a21b7ba627787c7c5f3f12f94; cookie_agree=allow-all; ka_push_skip=1',
}


def save_data(data):
    with open('actors.txt', 'w') as file:
        json.dump(data, file, ensure_ascii=False)


def get_page(url):
    response = request(url=url, headers=headers, method='GET')
    return response.text


def create_schedule_if_not(raw:str, film: Film, _cinema: Cinema) -> None:
    matches = re.findall(r'(?=(\d{2}:\d{2})\s*от (\d+) ₸)+', raw)
    for match in matches:
        time = match[0]
        price = match[1]
        if not Schedule.objects.filter(film=film, cinema=_cinema, time=time, price=price):
            Schedule.objects.create(film=film, cinema=_cinema, time=time, price=price)
        else:
            print('Такое расписание уже в базе данных')


def get_schedule(schedule_url, _cinema: Cinema):
    new_page = get_page(schedule_url)
    soup = BeautifulSoup(new_page, 'html.parser')
    film_names = soup.select('.showtimesMovie_name')
    session_times = soup.select('.showtimes_item .showtimes_sessions')
    if not film_names:
        return None
    for idx, film_name in enumerate(film_names):
        films_query = Film.objects.filter(name=film_name.text)
        if films_query:
            film = films_query[0]
        else:
            print(f'We do not have this film {film_name.text}')
            raise Film.DoesNotExist
        session = session_times[idx]
        raw = session.text
        create_schedule_if_not(raw, film, _cinema)


def get_base_information(text):
    soup = BeautifulSoup(text, 'html.parser')
    name = soup.select('.hat_title')[0].text
    address = soup.select('.theaterInfo_dataAddr')
    address = address[0].text if address else ''
    description = soup.select('.theaterInfo_descEditor')
    description = description[0].text if description else ''
    return name, address, description


def get_clean_links(text):
    soup = BeautifulSoup(text, 'html.parser')
    links = soup.select('.cinemaList_ref')
    links_clean = []
    for link in links:
        links_clean.append(link.get('href'))
    return links_clean


def main_loop(links_clean):
    for link in links_clean:
        text = get_page(link)
        name, address, description = get_base_information(text)
        try:
            _cinema = Cinema.objects.get(name=name)
        except:
            print(f'Добавленный новый кинотеатр {name}')
            continue
            _cinema = Cinema.objects.create(name=name, address=address, description=description)

        schedule_url = link + 'schedule'
        try:
            schedule = get_schedule(schedule_url, _cinema)
        except Film.DoesNotExist:
            continue
        if not schedule:
            print('У этого кинотеатра нет расписания')
            continue


if __name__ == '__main__':
    text = get_page('https://kz.kinoafisha.info/almaty/cinema/')
    links_clean = get_clean_links(text)
    main_loop(links_clean)
    populate_seats(create_all_new=True)