import re


def myGrep(fileName, subStr):
    with open(fileName) as textFile:
        for i in textFile:
            i = i.strip()
            if re.search(subStr, i):
                print(i)


myGrep('18_8.txt', 'line')

#
