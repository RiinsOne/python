import ogframework as og

######################################
"""
"""


######################################
"""
Упражнение 4.1
Создайте  в  отдельном  файле  функцию,
переводящую  градусы  по  шкале  Цельсия  в градусы
по шкале Фаренгейтапо формуле: TF= 9/5 * TC+ 32
"""


def convert_to_fahrent(cels):
    return 9 / 5 * cels + 32


print(convert_to_fahrent(30))
print(convert_to_fahrent(25))


######################################
"""
Упражнение 4.2
Создайтев отдельном файле функции,
вычисляющие площадь и периметр квадрата.
"""


def perimeter(a):
    return a * 4


def square(a):
    return a * a


og.newline()
print(perimeter(5))
print(square(4))


######################################
"""
Упражнение 4.3
Напишитефункцию в отдельном файле,
вычисляющую среднее арифметическое трех чисел.
"""


def triple(a, b, c):
    return (a + b + c) / 3


og.newline()
print(triple(2, 4, 6))


######################################
"""
Упражнение4.4Напишитефункцию в отдельном файле,
вычисляющую среднее арифметическое трех чисел.
Задайтезначения  по  умолчанию, в  момент  вызова
используйте  ключевые аргументы.
"""


def new_triple(a=5, b=5, c=5):
    return (a + b + c) / 3


og.newline()
print(new_triple(6, 8, 10))
print(new_triple())
#