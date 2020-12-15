from ogframework import newline

# Вариант 1

s = 'safk 411 far 1 rm 294'
lst = s.split()

lstInt = []
for i in lst:
    if i.isdigit():
        lstInt.append(int(i))

for i in lstInt:
    print(i)  # print(i, end=' ') - в ряд

countElements = 0
for i in lstInt:
    countElements += 1
print(countElements)

print(sum(lstInt))
print(max(lstInt))


# Вариант 2
newline()

S = '914ksak 129 skj -asi 9j k1j iojmju 9019489151 smaf14kla 01u'
lstS = []

for i in S:
    if i.isdigit():
        lstS.append(int(i))
print(lstS)

elements = 0
for k in lstS:
    elements += 1
print(elements)
print(max(lstS))
print(sum(lstS))

#
