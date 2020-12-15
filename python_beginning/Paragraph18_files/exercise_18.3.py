import urllib.request
import re

url = 'http://dfedorov.spb.ru/python/files/mbox-short.txt'

with open('mail.txt', 'w', encoding='utf-8') as newFile:
    newFile.write('')

with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        if re.search('@', str(line)):
            with open('mail.txt', 'a', encoding='utf-8') as outputFile:
                outputFile.write(f'{str(line)}\n')

#
