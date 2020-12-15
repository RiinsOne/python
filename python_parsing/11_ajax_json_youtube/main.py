import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r


def write_csv(data):
    with open('videos.csv', 'a', encoding='utf8', newline='') as f:
        order = ['name', 'url']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)


def get_page_data(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['content_html']

    soup = BeautifulSoup(html, 'lxml')

    items = soup.find_all('h3', class_='yt-lockup-title')

    for item in items:
        name = item.text.strip()
        url = item.find('a').get('href')

        data = {'name': name, 'url': url}
        write_csv(data)


def get_next(response):
    if 'html' in response.headers['Content-Type']:
        html = response.text
    else:
        html = response.json()['load_more_widget_html']

    soup = BeautifulSoup(html, 'lxml')

    try:
        url = 'https://youtube.com' + soup.find('button', class_='load-more-button').get('data-uix-load-more-href')
    except:
        url = ''

    return url


def main():
    # url = 'https://www.youtube.com/browse_ajax?ctoken=4qmFsgI6EhhVQ09tNF9BbkxQTEVCVnJiby0tTjdrUEEaHkVnWjJhV1JsYjNNZ0FEQUJPQUY2QVRLNEFRQSUzRA%253D%253D&continuation=4qmFsgI6EhhVQ09tNF9BbkxQTEVCVnJiby0tTjdrUEEaHkVnWjJhV1JsYjNNZ0FEQUJPQUY2QVRLNEFRQSUzRA%253D%253D&itct=CC4QybcCIhMI3qrirKbT5AIVTWeyCh2nBwoX'
    url = 'https://www.youtube.com/user/coolpropaganda/videos'
    # get_page_data(get_html(url))

    while True:
        response = get_html(url)
        get_page_data(response)

        url = get_next(response)

        if url:
            continue
        else:
            break


if __name__ == '__main__':
    main()
