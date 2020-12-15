# locals()
# globals()

animal = 'a'
def change_local():
    animal = 'w'
    print('locals: ', locals())

print(animal)  # a - глобальная переменная
change_local()  # locals:  {'animal': 'w'} - локальная переменная

print('globals: ', globals())  # выдаст все глобальные переменные, функции и тд
print(animal)  # a

#
