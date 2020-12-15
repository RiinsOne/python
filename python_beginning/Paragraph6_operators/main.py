import ogframework as og

print(type(True))  # <class 'bool'>

# 0.1 + 0.1 == 0.2  # True
# 0.1 + 0.1 + 0.1 = 0.3  # False

print(2 > 4)  # False
print(45 > 3)  # True
print(2 > 4 and 45 > 3)  # False
print(2 > 4 or 45 > 3)  # True

# Любое число, не равное нулю, или непустой объект - истина
# Числа, равные нулю, пустые объекты и None - ложь

og.newline()
print('' and 2)  # ''
print('' or 2)  # 2

og.newline()
y = 6 > 8
print(y)  # False
print(not y)  # True
print(not None)  # True
print(not 2)  # False

og.newline()
print(0 and 3)  # 0 - вернет первый ложный объект-операнд
print(5 and 4)  # 4 - вернет крайник правый объект-операнд

og.newline()
print(2 or 3)  # 2 - вернет первый истинный объект
print(None or 5)  # 5
print(None or 0)  # 0 - вернет оставшийся объект

og.newline()
print(2 + (4 > 8))  # 2

og.newline()
x = 0
print(-5 < x < 10)  # эквивалентно: line > -5 and line < 10

og.newline()
x = 5 < 10
y = 2 > 3
print(x or y)  # True
print((x or y) + 9)  # 10 - True равен 1
print(True + True + 2)  # 4

og.newline()
x1 = 1
print(x1 and 1 / x)  # 1.0

x2 = 0
print(x2 and 1 / x)  # 0


# функция ord() - определить, какое число соотв. символу
og.newline()
print(ord('L'))  # 76
print(ord('Ф'))  # 1060
print(ord('A'))  # 65
print('A' > 'L')  # False
print('Aa' > 'Ll')  # False

og.newline()
print('a' in 'abc')  # True
print('A' in 'abc')  # False
print('' in 'abc')  # True - пустая строка есть в любой строке
print('' in '')  # True





#
