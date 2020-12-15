def newline():
    print('\n')


# abs() - функция абсолютного значения
# pow(line, elem) - возведение в степень

# round(number) - возвращает число с плавающей точкой, до 0 цифр после запятой
# round(number[, ndigits]), где ndigits - число знаков после запятой
print(round(4.56666))  # 5
print(round(4.56666, 3))  # 4.567

# int() - возвращает целочисленный объект, построенный из числа или строки, или 0, если аргументы не переданы
# float() - возвращает число с плавающей точкой, построенное из числа или строки.
print(int(5.6))  # 5
print(int())  # 0
print(float(5))  # 5.0
print(float())  # 0.0

newline()
print(pow(abs(-5) + abs(-3), round(5.8)))
print(int(round(pow(round(5.777, 2), abs(-2)), 1)))

# help(abs) - посмотреть описание функции
help(abs)

newline()
deg_f = 80
print(deg_f)
print(5/9 * (deg_f - 32))


def convert_co_cels(fahren):
    return (fahren - 32) * 5/9


newline()
print(convert_co_cels(451))
print(convert_co_cels(300))


def func1(x):
    return x ** 4 + 4 * x


def func2(x, y):
    return y ** 4 + 4 * x


newline()
print(func1(2))
print(func2(2, 1))


newline()
a = 3  # глобальная переменная
print(f'Глобальная переменная a = {a}')  # пример использования f string
y = 8
print('Глобальная переменная elem =', y)  # обычный пример


def func():
    print(f'func: глобальная переменная a = {a}')
    y = 5  # локальная переменная
    print(f'func: локальная переменная elem = {y}')


func()
print(f'??? {y}')  # отобразится глобальная переменная


newline()
x = 50  # global variable


def change_global():
    global x  # indicate that line is a global variable
    print(f'x equals {x}')
    x = 2  # changing global variable
    print(f'Changing global variable x to {x}')


change_global()
print(f'The value of x is {x}')


def equation(x):
    c = 7
    return x + 8 + c


newline()
print(equation(4))
print(equation(9))
print(equation(3))


def summa(xx, yy):
    return xx + yy


newline()
f = summa  # присваиваем функцию переменной f
v = f(10, 3)  # вызываем функцию с другим именем
print(v)


def new_summa(xx, yy=2):
    return xx + yy


aa = new_summa(3)  # вместо elem подставляем значение по умолчанию
bb = new_summa(10, 40)  # теперь значение второго параметра равно 40
newline()
print(f'{aa}, {bb}')


def func2(f, a, b):
    return f(a, b)


newline()
v = func2(summa, 10, 3)  # передаем summa в качестве аргумента
print(v)


def func3(a, b=5, c=10):
    print(f'a equals {a}, b equals {b}, c equals {c}')


newline()
func3(3, 7)  # a=3, b=7, c=10
func3(25, c=24)  # a=25, b=5, c=24
func3(c=50, a=100)  # a=100, b=5, c=50




#
