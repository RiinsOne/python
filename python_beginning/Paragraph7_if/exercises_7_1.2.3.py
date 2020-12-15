import ogframework as og

######################################
"""
"""

# 7.1


def ph_func():
    value = float(input('Type pH value: '))
    if value == 1.0:
        print(f'{value} Juice')
    elif value == 2.0:
        print(f'{value} Shampoo')
    elif value == 3.0:
        print(f'{value} Soap')
    else:
        print('Not found')


ph_func()


######################################
# 7.2


def min_max():
    value1 = float(input('Type first number: '))
    value2 = float(input('Type second number: '))
    if value1 > value2:
        return value1
    else:
        return value2


og.newline()
print(min_max())


######################################
# 7.3


def even_func():
    value = int(input('Type int number: '))
    if value % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')


og.newline()
even_func()




#
