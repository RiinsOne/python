import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    r = requests.get(url)
    if r.ok:  # 200  ## 403 404
        return r.text
    print(r.status_code)


def under_over(find_by: str, data_list: list, tr: object):
    # find_by = 'Меньше' or 'Больше'
    tds = tr.find_all('td', {'data-sel': re.compile(find_by)})
    for td in tds:  
        pattern = f'Тотал {find_by.lower()}' + ' {}'
        pattern_name = td.find('div', class_='coeff-handicap').text.strip()
        name = pattern.format(pattern_name)
        rate = td.find('span').text.strip()
        data_list.append(
            (name, float(rate))
        )


def minus_plus(find_by: str, data_list: list, tr: object):
    # find_by = event_name[0] or event_name[1]
    tds = tr.find_all('td', {'data-sel': re.compile(find_by)})
    for td in tds:  
        pattern = f'{find_by}' + ' {}'
        pattern_name = td.find('div', class_='coeff-handicap').text.strip()
        name = pattern.format(pattern_name)
        rate = td.find('span').text.strip()
        data_list.append(
            (name, float(rate))
        )
            
    
def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    
    event_name = soup.find('div', class_='bg coupon-row').get('data-event-name').split(' - ')

    data_totals = []
    data_handicaps = []
    
    trs_totals = soup.find('div', {'data-mutable-id': 'Block_3'}).find('div', class_='market-inline-block-table-wrapper').find('table', class_='td-border table-layout-fixed').find_all('tr')
    
    trs_handicaps = soup.find('div', {'data-mutable-id': 'Block_2'}).find('div', class_='market-inline-block-table-wrapper').find('table', class_='td-border table-layout-fixed').find_all('tr')
    
    for tr in trs_totals[1:-2]:
        data_pairs = []
        
        under_over('Меньше', data_pairs, tr)
        under_over('Больше', data_pairs, tr)

        data_totals.append(data_pairs)
    
    for tr in trs_handicaps[1:]:
        data_pairs = []
        
        minus_plus(event_name[0], data_pairs, tr)
        minus_plus(event_name[1], data_pairs, tr)
        
        data_handicaps.append(data_pairs)
    
    for i in data_handicaps:
        print(i)
    for i in data_totals:
        print(i)
    print()
    
    
def main():
    url = 'https://www.marathonbet.ru/su/betting/Football/Russia'
    soup = BeautifulSoup(get_html(url), 'lxml')
    events = soup.find_all('div', class_='bg coupon-row')
    for event in events:
        try:
            link = 'https://www.marathonbet.ru' + event.find('a').get('href')
            get_page_data(get_html(link))
        except AttributeError:
            pass

    # url = 'https://www.marathonbet.ru/su/betting/Football/Russia/Premier+League/Zenit+St+Petersburg+vs+Arsenal+Tula+-+8235893'
    # get_page_data(get_html(url))


if __name__ == "__main__":
    main()
