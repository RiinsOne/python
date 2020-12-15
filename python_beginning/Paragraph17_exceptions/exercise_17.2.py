from random import randint

try:
    a = int(input('строки: '))
    b = int(input('столбы: '))
    c = int(input('диапазон от: '))
    d = int(input('диапазон до: '))

    lst = [[randint(c, d) for j in range(b)] for i in range(a)]
    for i in lst:
        print(i)

except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
else:
    print('Something happened')
finally:
    print('finally done')

#
