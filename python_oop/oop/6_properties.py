

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    # первый способ использовать геттеры и сеттеры,через свойство property
    # name = property(fget=get_name, fset=set_name)

    # второй способ через декоратор
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)

    # третий способ - передать геттер в свойство, а сеттер через экземпляр класса
    name = property(get_name)
    name = name.setter(set_name)


p = Person('Dima')


class PersonOne:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # name = property(name)


p1 = PersonOne('Riins')
