class Address():  # имя класса
    name = ""  # поля класса
    line1 = ""
    line2 = ""
    city = ""
    state = ""
    zip = ""


homeAddress = Address()

# заполняем поля объекта значениями:
homeAddress.name = "Orkhan Gasanov"
homeAddress.line1 = "701, N. C Street"
homeAddress.line2 = "Carver Science Building"
homeAddress.city = "Domodedovo"
homeAddress.state = "Moscow region"
homeAddress.zip = "142007"


vacationHomeAddress = Address()

vacationHomeAddress.name = "OG"
vacationHomeAddress.line1 = "Street"
vacationHomeAddress.line2 = "Carver Science Building"
vacationHomeAddress.city = "DME"
vacationHomeAddress.state = "Moscow"
vacationHomeAddress.zip = "142015"

print(f'Main address: {homeAddress.city}')
print(f'Vacation address: {vacationHomeAddress.city}')
print()


def printAddress(address):  # передаем в функцию объект
    print(address.name)  # выводим на экран поле объекта
    if len(address.line1) > 0:
        print(address.line1)
    if len(address.line2) > 0:
        print(address.line2)
    print(f'{address.city}, {address.state}, {address.zip}')


printAddress(homeAddress)
print()

printAddress(vacationHomeAddress)
print()

print()


class Dog():
    age = 0  # возраст собаки
    name = ""  # имя собаки
    weight = 0  # вес собаки
    # первым аргументом любого метода всегда является self, т.е. сам объект

    def bark(self):  # функция внутри класса называется методом
        # self.name - обращение к имени текущего объекта-собаки
        print(f'{self.name} говорит гав')


myDog = Dog()
myDog.name = "Didier"
myDog.weight = 6
myDog.age = 9

# вызовем метод bark() объекта myDog - собака подает голос:
myDog.bark()
Dog.bark(myDog)  # полная форма вызова метода myDog.bark()
# т.е. полная форма требует в качестве первого аргумента сам объект - self

#
