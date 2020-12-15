import urllib.request
import re

urlLink = 'http://dfedorov.spb.ru/python3/src/romeo.txt'


def histogram(url):
    mainDict = dict()
    rawLst = list()
    sortedLst = []

    with urllib.request.urlopen(url) as webText:
        for line in webText:
            line = line.strip()
            line = line.decode('utf-8')
            rawLst.append(line.split(' '))
    # print(rawLst)

    for i in rawLst:
        sortedLst += i
    # print(sortedLst)

    for word in sortedLst:
        if word not in mainDict:
            mainDict[word] = 1
        else:
            mainDict[word] += 1

    return mainDict


print(histogram(urlLink))

#
