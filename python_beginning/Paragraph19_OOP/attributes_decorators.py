class Ddd:
    def __init__(self, inputName):
        self.hiddenName = inputName

    @property
    def name(self):
        print('внутри getter')
        return self.hiddenName

    @name.setter
    def name(self, inputName):
        print('внутри setter')
        self.hiddenName = inputName


f = Ddd('I\'am OG')
print(f.name)
# внутри getter
# I'am OG

print()

f.name = 'TEST'
print(f.name)
# внутри setter
# внутри getter
# TEST
print()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)  # 5

# обращение к свойству diameter как к атрибуту
print(c.diameter)  # 10

c.radius = 7
# изменение атрибута radius привело к вычислению свойства diameter
print(c.radius)  # 7
print(c.diameter)  # 14

# приведет к ошибке, т.к. не указали метод set():
# c.diameter = 20  # AttributeError: can't set attribute

print()
print()


class Ddd5:
    def __init__(self, inputName):
        self.__hName = inputName

    @property
    def hName(self):
        return self.__hName

    @hName.setter
    def hName(self, inputName):
        self.__hName = inputName


ff = Ddd5('total_handicap message')
print(ff.hName)  # total_handicap message

ff.hName = 'event_more_view total_handicap message'
print(ff.hName)  # event_more_view total_handicap message

print(ff._Ddd5__hName)  # event_more_view total_handicap message










#
