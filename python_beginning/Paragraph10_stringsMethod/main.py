from ogframework import newline

print(type(0))  # <class 'int'>

print(str.capitalize('hello'))  # 'Hello'
print(str.center('hello', 20))  # '       hello        '

newline()
print('hello'.capitalize())  # 'Hello'

newline()
help(str.capitalize)  # вызвать help

newline()
print(('TTA' + 'G'*3).count('T'))  # 2

newline()
print('{0} and {1}'.format('labour', 'may'))  # labour and may
print('{1} and {0}'.format('labour', 'may'))  # may and labour

newline()
n = 10
print('{:b}'.format(n))  # 1010 - вывод в двоичной системе счисления
print('{:c}'.format(n))  # '\n' - вывод в формате Unicode
print('{:d}'.format(n))  # '10' - по основанию 10
print('{:x}'.format(n))  # 'a' - по основанию 16

newline()
print('spec'.startswith('a'))  # False
# проверяет, начинается ли строка с символа

ss = '              \n sssssss \n'
print(ss.strip())  # sssssss
# возвращает строку, очищенную от символа переноса строки (\n)
# и пробелов

newline()
print('Hello'.swapcase())  # hELLO

print('HELLO'.swapcase().endswith('o'))  # True
# в первую очередь вызывается метод swapcase, после endswith








#
