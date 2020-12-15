class Dog():
    name = ''
    # конструктор вызывается в момент создания объекта этого типа;
    # специальный метод Python, поэтому два нижних подчеркивания

    def __init__(self):
        print('A event_more_view dog was born!')


myDog = Dog()
print()


class Dog2():
    name = ''
    # Конструктор
    # Вызывается на момент создания объекта этого типа

    def __init__(self, newName):
        self.name = newName


myDog2 = Dog2('Didier')  # создаем собаку и устанавливаем её имя:
print(myDog2.name)  # вывести имя собаки, убедиться, что оно было установлено

# herDog = Dog2()  # будет ошибка, конструктору не передано имя

print()


class Dog3:  # () - pep8 ругается на скобки
    name = ''

    # Конструктор вызывается в момент создания объекта этого класса
    def __init__(self, newName):
        self.name = newName

    # Можем в любой момент вызывать метод и изменить имя собаки
    def setName(self, newName):
        self.name = newName

    # Можем в любой момент вызвать метод и узнать имя собаки
    def getName(self):
        return self.name


myDog3 = Dog3('Spot')  # создаем собаку с начальным именем
print(myDog3.getName())  # Spot - вызываем имя собаки

myDog3.setName('Didier')  # устанавлиаем новое имя
print(myDog3.getName())  # Didier - смотрим изменение имени

#
