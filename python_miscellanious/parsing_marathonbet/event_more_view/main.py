import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # results = soup.findAll("td", {"valign": "top"})
    totals = soup.find('div', {"data-mutable-id": "Block_3"}).find_all('tr', {"data-header-highlighted-bounded": "true"})
    under25 = totals[4].find('td', {"data-sel": re.compile('Меньше 2.5')})
    under25_value = under25.find('span').text
    print(under25_value)

    # print(total.find('td', re.compile('Меньше')).find('div').find('div', class_='coeff-price').find('span').text)

    # if total.find('div', class_='coeff-handicap').text == '(2.5)':
    #     print(total.find('span').text)
    #     # return total.find('span').text



def main():
    # url = 'https://www.marathonbet.ru/su/popular/Football/Russia'
    # soup = BeautifulSoup(get_html(url), 'lxml')
    # events = soup.find_all('div', class_='bg coupon-row')
    # for event in events:
    #     link = 'https://www.marathonbet.ru' + event.find('a').get('href')
    #     get_page_data(get_html(link))

    url = 'https://www.marathonbet.ru/su/betting/Football/Russia/Premier+League/Orenburg+vs+Rubin+Kazan+-+8235912'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
