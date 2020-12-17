from ogframework import newline

# s.upper() – возвращает строку в верхнем регистре
# s.lower() – возвращает строку в нижнем регистре
# s.title() – возвращает строку, первый символ которой в верхнем регистре
# s.find('вет', 2, 3) – возвращает позицию подстроки в интервале либо -1
# s.count('e', 1, 5) – возвращает количество подстрок в интервале либо -1
# s.isalpha() – проверяет, состоит ли строка только из букв
# s.isdigit() – проверяет, состоит ли строка только из чисел
# s.isupper() – проверяет, написаны ли все символы в верхнем регистре
# s.islower() – проверяет, написаны ли все символы в нижнем регистре
# s.istitle() – проверяет, начинается ли строка с большой буквы
# s.isspace() – проверяет, состоит ли строка только из пробелов

print('TT' + 'rr')  # 'TTrr'
print('TT'.__add__('rr'))  # 'TTrr'
print(str.__add__('TT', 'rr'))  # 'TTrr'

newline()
strOne = 'hi there man'

print(strOne.find('h', 1, -1))  # 4
print(strOne[-1])  # n - последний символ

#