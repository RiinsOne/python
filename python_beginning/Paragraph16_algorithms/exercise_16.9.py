from random import randint

lst = [randint(1, 10) for i in range(1, 21)]
print('list', lst)

summ = 0
tmpLst = list()

fstSct = 0
lstSct = 5
index = 0

for i in lst:
    if index == len(lst) - 4:
        break

    elif sum(lst[fstSct:lstSct]) > summ:
        summ = sum(lst[fstSct:lstSct])
        tmpLst = lst[fstSct:lstSct]
        print(f'index = {index}, summ = {summ}')
        print(f'index = {index}, tmlLst = {tmpLst}')

    fstSct += 1
    lstSct += 1
    index += 1

print()
print(summ)
print(tmpLst)

#
