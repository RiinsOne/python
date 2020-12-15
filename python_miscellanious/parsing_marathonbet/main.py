import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('mb.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Event name', 'Date', '1', 'X', '2', '1X', '12', 'X2', 'Handicap 1', 'Handicap 2', 'Total Under', 'Total Over'])
        writer.writerows(data)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    divs = soup.find_all('div', class_='bg coupon-row')

    main_data_list = []
    for line in divs:
        tmp_list = []
        team_name = line.get('data-event-name')
        tmp_list.append(team_name)

        event_date = line.find('table').find('tbody').find('tr').find('td').find('table').find('td', class_='date')
        tmp_list.append(event_date.text.strip())

        rates = line.find('table').find('tbody').find('tr').find_all('td')
        for rate in rates[8:]:
            tmp_list.append(rate.text.strip())

        main_data_list.append(tmp_list)

    write_csv(main_data_list)


def main():
    url = 'https://www.marathonbet.ru/su/popular/Football/Russia/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
