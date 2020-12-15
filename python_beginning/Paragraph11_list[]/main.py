from ogframework import newline
# списки могут содержать любые объекты

e = [56.8060, 57.1578, 57.4093, 56.1843, 57.2207]
print(e)
print(type(e))  # <class 'list'>
print(e[0])
print(e[1])
print(e[-1])  # last element

newline()
h = ['Hi', 27, -8.1, [1, 2]]
print(h)
h[1] = 'hello'  # меняем первый элемент списка
print(h)
print(h[1])

newline()
list1 = [5, 12, -25.1, 115]
print(len(list1))  # возвращает число (количество) элементов в списке
print(max(list1))  # возвращает максимальное значение, если все элементы числа
print(min(list1))  # минимальное значение
print(sum(list1))  # сумма значение в списке
print(sorted(list1))  # [-25.1, 5, 12, 115]
# возвращает копию списка, в котором элементы упорядочены по возрастанию
# Не изменяет список L


original = ['H', 'B', 'sdada']
final = original + ['T']
print(final)

newline()
final = final * 5
print(final)

del final[0]  # удалить первый элемент списка
print(final)


def unite(a, b):  # универсальная функция для складывания разных типов данных
    return a + b


newline()
print(unite([1, 2, 3], [4, 5, 6]))
print(unite('str1', 'str2'))
print(unite(4, 5))

newline()
list2 = ['bonjour', 7, 'hole', -1.2, 'privet']
if 7 in list2:
    print('The value is in the list')


newline()
g = list2[1:2]
print(g)  # 7 - включая элемент 1, не включая элемент 2


newline()
list3 = [-1, 1, 66.25, 333, 333, 1234.5]
del list3[0]  # удаляем первый элемент
print(list3)  # [1, 66.25, 333, 333, 1234.5]

del list3[2:4]  # удаляем 2 и 3 элемент включительно
print(list3)  # [1, 66.25, 1234.5]

del list3[:]  # удаление всех элементов в списке
print(list3)  # []


newline()
print(list2)
l2 = list2  # две переменные, содержащие одинаковые адреса памяти, называются псевдонимами
print(l2)
l2[0] = 111
print(l2)
print(list2)  # при изменении l2 изменится также и list2


newline()
x = y = [1, 2]  # создали псевдонимы
print(x is y)  # проверка, ссылаются ли переменные на один и тот же объект
# True

x2 = [3, 4]
y2 = [3, 4]
print(x2 is y2)  # False


# Поверхностное копирование - второй объект, содержит ссылки на элементы оригинала
newline()
listA = [4, 3, [2, 1]]
listB = listA[:]
print(listB is listA)  # False

listB[2][0] = -100  # меняем 2 элемент списка и 0 элемент вложенного списка, из которого состоит элемент 2
print(listB)
print(listA)
# списки разные, но элементы внутри ссылаются друг на друга


from copy import deepcopy
# import copy - модуль copy
# глубокое копирование - создается новый объект и рекурсивно создаются копии всех объектов

newline()
listC = deepcopy(listA)
print(listA is listC)  # False
print(listA)
print(listC)
listC[2][1] = 100
print(listC)  # [4, 3, [-100, 100]]
print(listA)  # [4, 3, [-100, 1]] - не изменился

#
