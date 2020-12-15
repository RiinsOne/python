import urllib.request
import re

urlLink = 'http://dfedorov.spb.ru/python3/sport.txt'

mainDict = dict()

with open('18_6.txt', 'w', encoding='utf-8') as newFile:
    newFile.write('')

with urllib.request.urlopen(urlLink) as textPage, open('18_6.txt', 'a', encoding='utf-8') as outfile:
    for line in textPage:
        line = line.decode('cp1251')
        outfile.write(line)

with open('18_6.txt', encoding='utf-8') as textFile:
    textFile.readlines(1)
    tmpLst = []
    strIndex = 1

    for i in textFile:
        i = i.strip()  # удалить \n на конце
        if not i.strip():  # удалить пустые строки
            continue
        tmpLst = i.split('\t')
        mainDict[strIndex] = tmpLst
        strIndex += 1

sportDict = dict()
sportInx = 1
tmpLst2 = []

for key in mainDict:
    # print('{}: {}'.format(key, mainDict[key]))
    mainDict[key][3] = mainDict[key][3].strip(' ')
    if not mainDict[key][3].strip():
        continue
    tmpLst = mainDict[key][3].split(',')

    sportDict[sportInx] = tmpLst
    sportInx += 1

lastDict = dict()

for key in sportDict:
    dictValue = sportDict[key]
    # print(f'{key}: {sportDict[key]}')
    for i in dictValue:
        i = i.strip()
        if i not in lastDict:
            lastDict[i] = 1
        else:
            lastDict[i] += 1

# for sport in lastDict:
#    print(f'{sport}: {lastDict[sport]}')

# print(type(lastDict['самбо']))  # <class 'int'>

countDict = dict()
firstIndexValue = 0
secondIndexValue = 0
thirdIndexValue = 0

# for i in lastDict:
#    print(f'{i}: {lastDict[i]}')

for i in lastDict:
    # print(f'{i}: {lastDict[i]}')
    if lastDict[i] > firstIndexValue:
        firstIndexValue = lastDict[i]

for i in lastDict:
    if lastDict[i] > secondIndexValue and lastDict[i] < firstIndexValue:
        secondIndexValue = lastDict[i]

for i in lastDict:
    if lastDict[i] > thirdIndexValue and lastDict[i] < secondIndexValue:
        thirdIndexValue = lastDict[i]

firstIndex = ''
secondIndex = ''
thirdIndex = ''

# print(thirdIndexValue)

for i in lastDict:
    if lastDict[i] == firstIndexValue:
        firstIndex = i
    if lastDict[i] == secondIndexValue:
        secondIndex = i
    if lastDict[i] == thirdIndexValue:
        thirdIndex = i

countDict[firstIndex] = firstIndexValue
countDict[secondIndex] = secondIndexValue
countDict[thirdIndex] = thirdIndexValue

for i in countDict:
    print(f'{i}: {countDict[i]}')

print('---------------------------')
sortedLst = sorted(lastDict, key=lastDict.get)
reversedLst = sortedLst[::-1]
print(reversedLst)
top3Lst = reversedLst[:3]
print(top3Lst)


#
