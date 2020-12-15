

name = 'OG'

class Person:
    name = 'Riins'

    @classmethod
    def change_name(cls, name):
        cls.name = name


p = Person()
print(p.__dict__)
p.change_name('sdsdsds')

print('Instance dict:', p.__dict__)
print('Person.name:', Person.name)

print('-----')


class PersonOne:
    def __init__(self, name):
        self.name = name

    @classmethod  # можно использовать как второй метод __init__
    def from_file(cls, path):
        with open(path) as f:
            name = f.read().strip()
        return cls(name=name)

    @classmethod
    def from_object(cls, obj):
        if hasattr(obj, 'name'):
            name = getattr(obj, 'name')
            return cls(name=name)
        return cls
