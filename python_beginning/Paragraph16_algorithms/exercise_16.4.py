from random import randint

lst = [randint(1, 100) for i in range(1, 1001)]

newLst = list()
for i in lst:
    if i > 1 and i % 2 != 0 and i % 3 != 0:
        newLst.append(i)
print('Список простых чисел: ', newLst)
print('Сумма простых чисел: ', sum(newLst))


#
