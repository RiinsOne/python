import ogframework as og

# 7.5


def bmi_func():
    m = float(input('Type your mass in kg: '))
    h = float(input('Type your height in meters: '))
    bmi = m / h ** 2
    print(f'Your Body Mass Index is {round(bmi, 2)}')


bmi_func()



#
