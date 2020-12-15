import re
import csv


def flightNumber(string):
    if re.search('FlightNumber', string):
        lst = string.split()
        index1 = lst[1].index('"') + 1
        index2 = lst[1][index1:].index('"') + index1
    value = lst[1][index1:index2]
    return value


def flightDate(string):
    if re.search('FlightDate', string):
        lst = string.split()
        index1 = lst[2].index('"') + 1
        index2 = lst[2][index1:].index('"') + index1
    value = lst[2][index1:index2]
    return value


f = open('newFunc.csv', 'w')
csvwriter = csv.writer(f)


with open('15216APR19CKP.XML') as xmlFile:
    strCounts = 0
    for i in xmlFile:
        row = []
        i = i.strip()
        # print(i)
        if re.search('<Flight FlightNumber', i):
            row.append(flightNumber(i))
        else:
            continue
        if re.search('<Flight FlightNumber', i):
            row.append(flightDate(i))
        else:
            continue
        strCounts += 1
        csvwriter.writerow(row)
        print(row)
    # print(strCounts)

f.close()



#
