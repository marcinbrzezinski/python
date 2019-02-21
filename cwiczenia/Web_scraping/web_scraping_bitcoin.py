import datetime
from contextlib import closing
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import pandas as pd


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


def get_previous_day(today):
    return today - datetime.timedelta(days=1)


def is_working_day(day):
    weekday = day.weekday()
    if weekday in range(5):
        return True
    else:
        return False


def to_string(_date):
    string = str(_date)
    replace = string.replace('-', '', 2)
    return replace


def get_dates(number, fd, wd):  # number = 10 ; fd - fromdate   ;   wd - working day (True or False)
    dates = []
    day = fd
    for num in range(number):
        day = day - datetime.timedelta(days=1)
        if wd:
            if is_working_day(day):
                dates.append(to_string(day))
        else:
            dates.append(to_string(day))
    return dates


def web_scraping(url):
    html_strumien = get_url(url)
    try:
        bs = BeautifulSoup(html_strumien, 'html.parser')
    except TypeError:
        return None
    else:
        for i, li in enumerate(bs.select('td')):
            # if i == 4:
            print(i, li.text)
            # return li.text.replace(' ', '').replace('\n', '').replace('s', '')


def add_row(_df, row):
    _df.loc[-1] = row
    _df.index += 1
    return _df.sort_index()


# df = pd.DataFrame(columns=['date', 'value'])
#
# any_day = datetime.datetime.today().date()
# working_day = True
# dates_list = get_dates(10, any_day, working_day)
#
# for date in get_dates(10, any_day, working_day):
#     value = web_scraping('https://coinmarketcap.com/historical/' + to_string(date))
#     add_row(df, [date, value])
#     print(date, value)
#
# print(df)

# print(get_previous_day(any_day))
# print(is_working_day(any_day), is_working_day(get_previous_day(any_day)))
# print(to_string(any_day))
# print(get_dates(10, any_day, working_day))

web_scraping('https://coinmarketcap.com/historical/20180101')