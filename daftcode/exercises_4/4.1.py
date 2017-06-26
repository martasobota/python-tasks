"""
Link to task description [PL]:
https://github.com/daftcode/zajecia_python_mini_edycja3/tree/master/zajecia_4
"""

import requests
from bs4 import BeautifulSoup

def get_lucky_nums():
    LOTTO_URL = "http://www.lotto.pl/lotto/wyniki-i-wygrane/wyszukaj"
    LOTTERY_DATA = {
        'data_losowania[date]':'2017-06-22',
        'op':'',
        'value': '2017-06-22',
        'form_build_id':'form-cb5acd34f82b21c3cbad2ad4ad5110df',
        'form_id':'lotto_wyszukaj_form'
    }

    r = requests.post(LOTTO_URL, data=LOTTERY_DATA)
    soup = BeautifulSoup(r.text, 'html.parser')

    lotto_results = list()

    for lotto in soup.find_all('div', attrs={'class': 'sortrosnaco 5960-kolejnosc', 'class': 'wynik_lotto'})[:6]:
        lotto_results.append(lotto.get_text())

    message = "Lucky lotto numbers for {} are: {}".format(LOTTERY_DATA['value'], ', '.join(map(str, lotto_results)))
    return message

print(get_lucky_nums())