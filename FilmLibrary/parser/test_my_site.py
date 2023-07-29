import requests
from bs4 import BeautifulSoup

s = requests.get('https://kz.kinoafisha.info/almaty/movies/name/').text
# s = requests.get('http://127.0.0.1:8000/movies/').text
soup = BeautifulSoup(s, 'html.parser')
names = []
for link in soup.select('.movieItem_title'):
    l = link.text
    names.append(l)
    # if l:
    #     url = 'http://127.0.0.1:8000/' + l
    # else:
    #     continue
    # st = requests.get(url)
    # if st.status_code != 200:
    #     print(st, st.url)
print(names)