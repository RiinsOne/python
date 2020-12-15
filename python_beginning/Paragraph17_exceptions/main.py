# x = int(input())
x = 0
if x == 0:
    print('Error!')
else:
    print(5/x)

print()

# try:
try:
    a = 5
    # a = int(input('Enter a number: '))
    print(5/a)
except:
    print('Error dividing by zero')

print()

# print(4/0)  # ZeroDivisionError: division by zero
# ошибка - ZeroDivisionError

# print(int('r'))  # ValueError: invalid literal for int() with base 10: 'r'
# ошибка - ValueError

try:
    b = 7
    # b = int(input('Enter a number: '))
    print(5/b)
except ZeroDivisionError:  # указываем тип исключения
    print('Error dividing by zero')
except ValueError:
    print('Error converting to a number')


print()

try:
    d = 5
    # d = int(input('type: '))
    print(5/d)
except ZeroDivisionError as z:
    print('Обрабатываем исключение - деление на ноль!')
    print(z)  # выводим на экран информацию об исключении
except ValueError as v:
    print('Обрабатываем исключение - преобразование типов!')
    print(v)
else:
    print('Выполняется, если не произошло исключительных ситуаций!')
finally:
    print('Выполняется всегда и в последнюю очередь!')

print()


def list_find(lst, target):
    try:
        index = lst.index(target)
    except ValueError:  # ValueError: value is not in list
        index = -1
    return index


print(list_find([3, 5, 6, 7], 5))  # 1
print(list_find([3, 5, 6, 7], 7))  # 3
print(list_find([3, 5, 6, 7], -5))  # -1
print(list_find([3, 5, 6, 7], 'd'))  # -1

#
