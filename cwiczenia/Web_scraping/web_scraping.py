from contextlib import closing
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup


def czy_poprawna(response):
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)  # sprawdza czy jest to html


def get_url(url):
    try:
        with closing(get(url, stream=True)) as response:
            if czy_poprawna(response):
                return response.content
            else:
                return None
    except RequestException as err:  # obsluga błędu w adresie
        print(err)
        print('Nieodpowiedni link')


# print(get_url("https://www.nbp.pl/Kursy/KursyC.html"))
# print(get_url("qwerrt"))

html_strumien = get_url("https://www.nbp.pl/Kursy/KursyC.html")
bs = BeautifulSoup(html_strumien, 'html.parser')
for i, li in enumerate(bs.select('td')):
    print(i, li.text)
