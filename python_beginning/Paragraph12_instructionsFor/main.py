from ogframework import newline

num = [0.8, 7.0, 6.8, -6]

for i in num:
    print(i, '- number')

# for перебирает все элементы указанного списка или строки
# цикл сработает ровно столько раз, сколько элементов находиться в списке

newline()
for i in [1, 2, 'hi']:
    print(i)

newline()
for i in 'string':
    print(i)

newline()
for i in num:
    if i == 7.0:
        print(i, '- number 7.0')

newline()
country = 'Russia'
for char in country:
    if char.isupper():
        print(char)


newline()
# Функция range
print(range(0, 10, 1))  # range(0, 10)
print(range(10))  # range(0, 10)
# конечное значение не включительно
# range(10) - 0 1 2 3 4 5 6 7 8 9, без 10

for i in range(0, 10, 1):
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9 - вывод в ряд, пробел как разделитель

newline()
for i in range(10):
    print(i, end='*')  # 0*1*2*3*4*5*6*7*8*9*

newline()
for i in range(2, 20, 2):
    print(i, end=' ')

newline()
for i in range(20, 2, -2):
    print(i, end=' ')

newline()
print(list(range(0, 6)))  # [0, 1, 2, 3, 4, 5]
print(sum(list(range(0, 6))))  # 15
# list(range(0, 6) - создать список в диапазоне от 0 до 5 включительно

print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]

# sum() для списка - подсчитает сумму всех элементов списка


# меняем список lst2, каждый индекс умножаем на 2
newline()
lst2 = [4, 10, 5, -1.9]
print(lst2)
for i in range(len(lst2)):  # len(lst2) - 4, но range(4) от 0 до 3 включительно
    lst2[i] *= 2  # сокращенный вариант
    # lst2[i] = lst2[i] * 2
print(lst2)  # [8, 20, 10, -3.8]


#
