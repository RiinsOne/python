import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    # 1,647 total ratings
    r = s.split(' ')[0]
    result = r.replace(',', '')
    return result


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)
        
        writer.writerow((data['name'],
                         data['url'],
                         data['reviews']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[3]
    plugins = popular.find_all('article')  # 4
    
    for plugin in plugins:
        name = plugin.find('h2').text
        url = plugin.find('h2').find('a').get('href')
        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)
        print(rating)
        
        data = {'name': name,
                'url': url,
                'reviews': rating}
        
        write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()
