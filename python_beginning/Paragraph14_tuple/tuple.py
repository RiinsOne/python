# Кортежи

# Кортеж, условно, неизменяемый список, т.к. применимы
# многие списковые функции, кроме изменения

# Кортежи используют, когда мы хотим быть уверены, что элементы
# структуры данных не будут изменены в процессе работы программы

a = ()  # создание пустого кортежа
print(a)  # ()

A = (4)  # это не кортеж, а целочисленный объект
print(A)  # 4

b = (4,)  # это уже кортеж, состоящий из одного элемента
print(b)  # (4,)

B = ('1', 2, '4')
print(B)  # ('1', 2, '4')
print(len(B))  # 3

c = tuple(range(5))
print(c)  # (0, 1, 2, 3, 4)

C = c + B  # слияние кортежей
print(C)  # (0, 1, 2, 3, 4, '1', 2, '4')

d = tuple([1, 5, 6, 7, 8, '1'])  # кортеж из списка
print(d)  # (1, 5, 6, 7, 8, '1')


print()
print()

(x, y) = (10, 5)
print(x)  # 10
print(y)  # 5

x, y = 1, 3  # если убрать круглые скобки, то результат не изменится
print(x)  # 1
print(y)  # 3

print()
x, y = y, x
print(x)  # 3
print(y)  # 1

print()
# кортеж изменить нельзя, но можно изменить список, входящий в кортеж
t = (1, 4, [2, 7], 's', 'd')
print(t[2])  # [2, 7]
t[2][0] = 'changedOne'
print(t)  # (1, 4, ['changedOne', 7], 's', 'd')

#
