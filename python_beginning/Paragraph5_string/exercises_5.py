import ogframework as og

######################################
"""
"""


######################################
"""
Упражнение 5.1
Попросите пользователя ввести свое имя и после этого
отобразите на экране строку вида:
Привет, <имя>!Вместо <имя>должно указываться то,
что  пользователь  ввел  с клавиатуры.
"""

ask_name = input('What is your name: ')
print(f'Hi there, {ask_name}')


######################################
"""
Упражнение 5.2
Напишите программу, определяющую сумму и
произведение трех чисел (типа int, float),
введенных с клавиатуры.
"""

def func():
    a = float(input('Type first number: '))
    b = float(input('Type second number: '))
    c = float(input('Type third number: '))
    print(f'The sum of numbers: {a + b + c}')
    print(f'The product of numbers: {a * b * c}')


og.newline()
func()


#
