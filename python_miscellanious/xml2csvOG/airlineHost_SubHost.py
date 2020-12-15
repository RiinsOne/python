import re

xf = 'xmlfile.XML'
hostList = list()

with open(xf) as f:
    for i in f:
        i = i.strip()
        if re.search('<Airline', i):
            hostList.append(i)

for i in hostList:
    print(i)
    print(hostList.index(i))
