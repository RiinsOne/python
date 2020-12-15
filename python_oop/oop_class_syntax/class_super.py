class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b


class Square(Rectangle):
    def __init__(self, a):
        b = a
        super().__init__(a, b)
        self.c = 'red'


s = Square(10)
print(s.a)  # 10
print(s.b)  # 10
print(s.c)  # 'red'

#


class Vehicle:
    def __init__(self):
        self.milage = 0

    def get_speed(self):
        return 100


class Car(Vehicle):
    def __init__(self):
        super().__init__()  # наследовать параметры инстанс класса
        self.seating_count = 0

    def get_speed(self):
        s = super().get_speed()
        print(s)
        return s * 2


c = Car()
print(c.milage)
print(c.seating_count)
print()

c.get_speed()  # 100
print(c.get_speed())  # 200

#
