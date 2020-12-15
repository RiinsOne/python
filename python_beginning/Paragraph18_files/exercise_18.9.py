import re
import urllib.request


def links(url):
    linkCounts = 0
    with urllib.request.urlopen(url) as webpage:
        for line in webpage:
            line = line.decode('utf-8')
            line = str(line)
            line = line.strip()
            if re.search('</a>', line):
                print(line)
                linkCounts += 1
    return linkCounts


urlLink = 'https://mail.ru/'

print(links(urlLink))

#
