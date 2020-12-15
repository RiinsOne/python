import urllib.request
import re

url = 'http://dfedorov.spb.ru/python/files/p.html_css'

with open('18_4.txt', 'w', encoding='utf-8') as newFile:
    newFile.write('')

with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')

        p = re.compile(r'<.*?>')
        clean = p.sub('', line)

        if not clean.strip():
            continue
        with open('18_4.txt', 'a', encoding='utf-8') as outputFile:
            outputFile.write(f'{clean}\n')


p = re.compile(r'<.*?>')
print(p.sub('', url))

"""
cleanr = re.compile('<.*?>')
cleanText = re.sub(cleanr, '', url)
print(cleanText)
"""

#
