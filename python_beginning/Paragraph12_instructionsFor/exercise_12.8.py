from ogframework import newline

# Вариант 1

s = 'this is some text, try to find the longer word'
lst = s.split()
lst2 = []

for i in lst:
    lst2.append(str(len(i)))

indexLst = 0
for i in lst2:
    if i.isdigit():
        indexLst = max(lst2)

element = str(indexLst)
print(lst2.index(element))


# Вариант 2
newline()

S = 'this is XXXXXXXXX some text, try to find the longer word'
lstS = S.split()
longest = ''

for k in lstS:
    if len(k) > len(longest):
        longest = k
indexLstS = lstS.index(longest)
print(indexLstS)

#
