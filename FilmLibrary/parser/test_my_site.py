import requests
from bs4 import BeautifulSoup

s = requests.get('http://127.0.0.1:8000/movies/').text
soup = BeautifulSoup(s, 'html.parser')
for link in soup.select('.btn'):
    l = link.get('href')
    if l:
        url = 'http://127.0.0.1:8000/' + l
    else:
        continue
    st = requests.get(url)
    if st.status_code != 200:
        print(st, st.url)
