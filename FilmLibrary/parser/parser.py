import json
import re
import random
import populate_db

from django.utils.text import slugify
from requests import request
from bs4 import BeautifulSoup
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


def get_links(text) -> list:
    soup = BeautifulSoup(text, "html.parser")
    all_person = soup.select('.persons_names  a')
    links = []
    for link in all_person:
        links.append(link.get('href'))
    return links



def get_biography(soup):
    # all_person = soup.select('.visualEditorInsertion p')
    biography = ''
    for paragraph in soup:
        try:
            text = paragraph.text
            clean_text = text.replace('\n', ' ')
            biography += clean_text
        except:
            return biography
    return biography
def person_detail_page(url):
    pesons_details_raw = get_page(url)
    person_data = {}
    soup = BeautifulSoup(pesons_details_raw, "html.parser")
    info_tab = soup.select('.personMainTab_infoItem')
    a = 5
    try:
        name = soup.select('.hat_title')[0].text
        slug = slugify(name) if name else None
        date_of_birth = soup.select('.personMainTab_infoItem')[0].contents[3].text if \
            soup.select('.personMainTab_infoItem')[0].contents[1].text == 'Дата рождения' else None
        age = soup.select('.personMainTab_infoItem')[1].contents[3].text if \
            soup.select('.personMainTab_infoItem')[1].contents[1].text == 'Возраст' else None
        career = soup.select('.personMainTab_infoItem')[3].contents[3].text if \
            soup.select('.personMainTab_infoItem')[3].contents[1].text == 'Карьера' else ''
        image_url = soup.select('.personMainTab_posterPicture .picture_image')[0]['src']
    except IndexError:
        return
    model = None
    bio_select = soup.select('.visualEditorInsertion p')
    biography = get_biography(bio_select)
    if re.search(r"актер|актриса", career, re.IGNORECASE):
        model = 'Actor'
    elif re.search(r"Режиссер|продюсер|сценарист", career, re.IGNORECASE):
        model = "Director"
    fields = (name, slug, date_of_birth, age, career, model, image_url)
    if not all(fields):
        print('Miss some data going for other person')
        return
    else:
        person_data['name'] = name
        person_data['slug'] = slug
        person_data['date_of_birth'] = date_of_birth
        person_data['age'] = age
        person_data['biography'] = biography
        person_data['model'] = model
        person_data['career'] = career
        person_data['image_url'] = image_url
    person_data_in_page[person_detail_page.index] = person_data
    person_detail_page.index += 1
    print(person_data['name'])

if __name__ == '__main__':
    text = get_page(r'https://www.kinoafisha.info/person/')
    soup = BeautifulSoup(text, 'html.parser')
    pagination = soup.select('.bricks-line .bricks_item')
    person_detail_page.index = 1
    for page in pagination[4:]:
        person_data_in_page = {}
        url = page['href']
        text = get_page(url)
        all_person_links = get_links(text)
        for link in all_person_links:
            person_detail_page(link)
        populate_db.save(person_data_in_page)
    # save_data(person_data_in_page)

