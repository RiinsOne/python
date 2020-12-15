import urllib.request

url = 'http://dfedorov.spb.ru/python/files/tutchev.txt'
urlImage = 'http://dfedorov.spb.ru/python/files/tutchev.jpg'


def generateHtmlfirstHalf():
    htmlMain = '<!DOCTYPE html_css>'
    headTag = '<head>\n' \
            '<meta charset=\'utf-8\'>\n' \
            '<title>Tutchev</title>\n' \
            '</head>'
    htmlTag = f'{htmlMain}\n' \
        f'<html_css>\n' \
        f'{headTag}\n' \
        f'<body>\n' \

    with open('exercise_18.2.html_css', 'w', encoding='utf-8') as output_file:
        output_file.write(f'{htmlTag}')


def generateHtmlSecondHalf():
    htmlTag = f'\n</body>\n' \
        f'</html_css>\n'

    with open('exercise_18.2.html_css', 'a', encoding='utf-8') as output_file:
        output_file.write(f'{htmlTag}')


def imgScrP(link):
    p = f'<p>' \
        f'<img src=\'{link}\' alt=\'Tutchev\'>' \
        f'</p>'
    return p


with open('exercise_18.2.txt', encoding='utf-8') as fileTxt:
    firstLineLst = fileTxt.readlines(1)
    firstLine = ''.join(firstLineLst)


def bodyWebPage(textLink):
    with open('exercise_18.2.html_css', 'a', encoding='utf-8') as output_file:
        output_file.write(f'<p>\n'
                          f'{firstLine}'
                          f'</p>\n')

    with urllib.request.urlopen(textLink) as webpage:
        lst = list()
        for line in webpage:
            line = line.strip()
            line = line.decode('utf-8')
            lst.append(line)

        for i in lst[2:]:
            with open('exercise_18.2.html_css', 'a', encoding='utf-8') as output_file:
                output_file.write(f'{i}<br>\n')


    with open('exercise_18.2.html_css', 'a', encoding='utf-8') as outputImage:
        outputImage.write(imgScrP(urlImage))


def importToTxt(textLink):
    with open('exercise_18.2.txt', 'w', encoding='utf-8') as outputImage:
        outputImage.write('')

    with urllib.request.urlopen(textLink) as txt:
        for line in txt:
            line = line.strip()
            line = line.decode('utf-8')

            with open('exercise_18.2.txt', 'a', encoding='utf-8') as output_file:
                output_file.write(f'{line}\n')


importToTxt(url)
generateHtmlfirstHalf()
bodyWebPage(url)
generateHtmlSecondHalf()






#
