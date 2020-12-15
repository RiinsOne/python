import ogframework as og

# \n -переход на новую строку
# \t -знак табуляции
# \\ -наклонная черта влево
# \' -символ  одиночной кавычки
# \" -символ  двойной кавычки

# len() - определяет длину строки
help(len)

print(len('hello!'))  # 6
print('hi ' + 'there ' + 'guys')

og.newline()
word = 'Mars'
numeral = 5
print(word + str(numeral))  # преобразуем число в строку

print(int('-5'))  # обратное преобразование

print('spam' * 10)

print("Hello's")
print('Hello\'s')
print(len('\''))  # 1


print('''Это длинная  # 'Это длинная\nстрока'
строка''')
print('This is a long\nstring')

og.newline()
print(1, 3, 5)
print(1, '2', 'string again', 56)

og.newline()
print(1, 6, 7, 8, 9)
print(1, 6, 7, 8, 9, sep=':')

############################

# s = input('Type something: ')  # ввести значение с клавиатуры
# print(s)
# print(type(s))  # <class'str'>  # функция input() возвращает строковый объект

# og.newline()
# s = int(input('Type any number: '))
# print(s + 5)


og.newline()
another_string = 'I like to programming!'
print(another_string[0])
print(another_string[-1])
print(len(another_string) - 1)  # 21 - индекс последнего символа
print(another_string[20])

# строки и числа являются неизменяемыми

og.newline()
str1 = 'Pythons are found in Africa'
print(str1[1:3])  # 'yt'

og.newline()
print(str1[:3])  # Pyt - с 0 индекса по 3-ий не включительно
print(str1[:])  # вся строка
print(str1[::2])  # Ptosaefudi fia - третий аргумент задает шаг (по умолчанию один)
print(str1[::-1])  # обратный шаг
print(str1[:-1])  # строка без последнего символа
print(str1[-1:])  # последний индекс
print(str1[1:])  # выведет всю строку без нулевого индекса

og.newline()
str2 = 'I like make programs'
print(str2)
print('J' + str2[1:])  # 'J' + строка без нулевого индекса


#
