from bs4 import BeautifulSoup
import parser


page = parser.get_page('https://www.kinoafisha.info/person/8404825/')
soup = BeautifulSoup(page, "html.parser")
all_person = soup.select('.visualEditorInsertion p')
biography = ''
for paragraph in all_person:
    text = paragraph.text
    clean_text = text.replace('\n', '* ')
    biography += clean_text
parser.save_data(biography)