from ogframework import newline

s = 'Строка для изменения'
print(list(s))  # ['С', 'т', 'р', 'о', 'к', 'а', ' ', 'д', 'л', 'я', ' ', 'и', 'з', 'м', 'е', 'н', 'е', 'н', 'и', 'я']

lst = list(s)  # функция list() пытается преобразовать аргумент в список
lst[0] = 'S'  # изменяем список, полученный из строки
print(lst)

newS = ''.join(lst)  # преобразуем список в строку с помощью строкового метода join()
# newS = str.join('', list3)  # тоже самое
print(newS)  # Sтрока для изменения

newline()
A = ['red', 'green', 'blue']
print(' '.join(A))  # red green blue
print(''.join(A))  # redgreenblue
print(str.join('***', A))  # red***green***blue

newline()
n = 734853847538
n = str(n)  # преобразуем число в строку
print(n)  # '734853847538'
print(type(n))  # <class 'str'>
print(list(n))  # ['7', '3', '4', '8', '5', '3', '8', '4', '7', '5', '3', '8']
# print(list(str(n))) - можно было и так в самом начале

newline()
string = 'd a dd dd gg rr tt yy rr ee'
print(string)  # d a dd dd gg rr tt yy rr ee
string2 = string.split()
# split() - строковый метод, преобразует строку в список,
# если строка содержит разделитель, "пробел" по умолчанию
print(string2)  # ['d', 'a', 'dd', 'dd', 'gg', 'rr', 'tt', 'yy', 'rr', 'ee']

newline()
newString = 'd:a:dd:dd:gg:rr:tt:yy:rr:ee'
newString2 = newString.split(':')
print(newString)
print(newString2)  # ['d', 'a', 'dd', 'dd', 'gg', 'rr', 'tt', 'yy', 'rr', 'ee']


newline()
# Nested Lists - Вложенные списки

list1 = [['A', 1], ['B', 2], ['C', 3]]
print(list1)
print(list1[0])  # ['A', 1]
print(list1[0][0])  # 'A'
print(list1[1][1])  # 2


#
