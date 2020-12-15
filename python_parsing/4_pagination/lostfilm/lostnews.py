import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:  # 200  ## 403 404
        return r.text
    print(r.status_code)


def refine_cy(s):
    # ТИЦ: 3 -> ['ТИЦ:', '3']
    return s.split(' ')[-1]


def write_csv(data):
    with open('4_pagination/lostfilm/lostfilm.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((
            data['name'],
            data['url'],
            data['snippet'],
            data['cy']
        ))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    
    lis = soup.find_all('a', class_='row no-decoration')
    
    for li in lis:
        try:
            name = li.find('div', class_='news-title').text
        except:
            name = ''
        
        try:
            url = 'https://www.lostfilm.tv' + li.get('href')
        except:
            url = ''
        
        try:
            snippet = li.find('div', class_='news-text').text.strip()
        except:
            snippet = ''
        
        try:
            c = 'ТИЦ: ' + li.find('div', class_='comment-blue-box').text.strip()
            cy = refine_cy(c)
        except:
            cy = ''
    
        data = {
            'name': name,
            'url': url,
            'snippet': snippet,
            'cy': cy
        }
        
        write_csv(data)


def main():
    pattern = 'http://www.lostfilm.tv/news/page_{}/type_0'
    
    for i in range(1, 6):  # [1, 2, 3, 4, 5]
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__ == "__main__":
    main()
