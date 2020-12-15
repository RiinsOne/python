from ogframework import newline

L = [3, 'hello', 7, 4, 'привет', 4, 3, -1]

hi = 'привет'

if hi in L:
    L.remove(hi)
    print(L)
else:
    L.append(hi)
    print(L)

newline()
count = L.count(4)
print(count)

if count > 1:
    L.clear()
print(L)


#
