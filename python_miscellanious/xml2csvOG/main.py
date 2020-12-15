import re
import csv

# f = open('newFunc.csv', 'w')
# csvwriter = csv.writer(f)
# csvwriter.writerow(row)
# f.close()

xf = 'xmlfile.XML'

tmpStr = '<Airline Host="152" SubHost="YY">'


def defFunc(rowStr):
    if re.search('=', rowStr):
        vleIdx1 = rowStr.index(' ') + 1
        vleIdx2 = rowStr[vleIdx1:].index('=') + vleIdx1
        atrIdx1 = rowStr.index('"') + 1
        atrIdx2 = rowStr[atrIdx1:].index('"') + atrIdx1
    vle1 = rowStr[vleIdx1:vleIdx2]
    atr1 = rowStr[atrIdx1:atrIdx2]

    rowStr = rowStr[atrIdx2 + 1:]

    if re.search('=', rowStr):
        vleIdx1 = rowStr.index(' ') + 1
        vleIdx2 = rowStr[vleIdx1:].index('=') + vleIdx1
        atrIdx1 = rowStr.index('"') + 1
        atrIdx2 = rowStr[atrIdx1:].index('"') + atrIdx1
    vle2 = rowStr[vleIdx1:vleIdx2]
    atr2 = rowStr[atrIdx1:atrIdx2]

    return (vle1, atr1), (vle2, atr2)


def getHead(string):
    def iterFc(rowStr, lst):
        if not re.search('=', rowStr):
            return lst
        else:  # re.search('=', rowStr):
            vleIdx1 = rowStr.index(' ') + 1
            vleIdx2 = rowStr[vleIdx1:].index('=') + vleIdx1
            atrIdx1 = rowStr.index('"') + 1
            atrIdx2 = rowStr[atrIdx1:].index('"') + atrIdx1
        vle1 = rowStr[vleIdx1:vleIdx2]
        lst.append(str(vle1))
        rowStr = rowStr[atrIdx2 + 1:]
        return iterFc(rowStr, lst)
    return iterFc(string, list())


headLst = []
with open(xf) as xmlFile:
    for line in xmlFile:
        line = line.strip()
        for i in getHead(line):
            if i not in headLst:
                headLst.append(i)


print(headLst)

newLst = list()
with open(xf) as file:
    for line in file:
        line = line.strip()
        if not re.search('=', line) and not re.search('</', line):
            if line not in newLst:
                newLst.append(line)

print(newLst)


def getLongHead(string):
    if re.search(' ', string):
        spcIdx = string.index(' ')
        mainVle = string[1:spcIdx]

    def iterFc(rowStr, lst):
        if not re.search('=', rowStr):
            return lst
        else:  # re.search('=', rowStr):
            vleIdx1 = rowStr.index(' ') + 1
            vleIdx2 = rowStr[vleIdx1:].index('=') + vleIdx1
            atrIdx1 = rowStr.index('"') + 1
            atrIdx2 = rowStr[atrIdx1:].index('"') + atrIdx1
        vle = rowStr[vleIdx1:vleIdx2]
        lst.append(f'{mainVle}/{vle}')
        rowStr = rowStr[atrIdx2+1:]
        return iterFc(rowStr, lst)
    return iterFc(string, list())


print()
print(tmpStr)
getLongHead(tmpStr)
print(getLongHead(tmpStr))


headLongLst = []
with open(xf) as xmlFile:
    for line in xmlFile:
        line = line.strip()
        for i in getLongHead(line):
            if i not in headLongLst:
                headLongLst.append(i)

print()
print(headLongLst)




