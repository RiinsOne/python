# сумма чисел в диапазоне от 1 до 100:

total = 0
for i in range(1, 101):
    total += i  # total = total + i
print(total)

# более красивое решение данной задачи
a = sum(list(range(1, 101)))
print(a)

#
