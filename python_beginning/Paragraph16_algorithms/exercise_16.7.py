from random import randint

lst = [randint(1, 100) for i in range(1, 1001)]
print('list', lst)

hundredPercent = len(lst)
print(hundredPercent)

average = round(sum(lst) / len(lst))
print(average)

count = 0
for i in lst:
    if i > average:
        count += 1
print(count)

percent = count * 100 / hundredPercent
print(f'Процентное содержание элементов,'
      f'превышающих средне.ариф. равно = {percent}%')

#
