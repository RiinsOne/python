import math

class Point:
    def __init__(self, x=0, y=0):  # конструктор устанавливает координаты
        self.x = x
        self.y = y

    def __eq__(self, other):  # метод для сравнения двух точек
        return self.x == other.x and self.y == other.y

    def __str__(self):  # метод для строкового вывода информации
        # return '({0.x}, {0.y})'.format(self)
        return f'({self.x}, {self.y})'

    def func(self):  # понадобится в следующем примере
        return abs(self.x-self.y)


a = Point()  # создаем объект, по умолчанию x=0, y=0
print(a)  # (0, 0)
print(str(a))  # (0, 0)  # здесь вызывается метод __str__() класса Point
# полная форма Point.__str__(a)
print()

b = Point(3, 4)
print(str(b))  # (3, 4)
b.x = -19
print(a.func())  # 0
print(str(b))  # (-19, 4)

print(a == b, a != b)  # вызывается метод __eq__()
# False True
# полная форма для сравнения a== b имеет вид: Point.__eq__(a, b)

print()
print()


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)  # вызов конструктора базового класса
        self.radius = radius

    def area(self):  # площадь окружности
        return math.pi * (self.radius ** 2)

    def circumference(self):  # длина окружности
        return 2 * math.pi * self.radius

    def __eq__(self, other): # сравнение двух окружностей
        return self.radius == other.radius and super().__eq__(other)

    def __str__(self):  # вывод информации в виде строки
        return f'({self.radius}, {self.x}, {self.y})'
        # return "({0.radius}, {0.x}, {0.y})".format(self)


circle = Circle(2)  # создаем объект, radius=2, x=0, y=0
circle.radius = 3
circle.x = 12
a = Circle(4, 5, 6)
b = Circle(4, 5, 6)
print(str(a))  # здесь вызывается специальный метод __str__()
# (4, 5, 6)

print(str(b))  # (4, 5, 6)
print(a == b)  # True  # здесь вызывается специальный метод __eq__()
# полная форма вызова метода для a == b: Circle.__eq__(a, b)
print(a == circle)  # False
print(a != circle)  # True  # отрицание результат вызова метода __eq__()
print()

# вызов метода базового класса из дочернего называется полиморфизмом:
print(circle.func())  # 12

# таблица специальных методов
# https://docs.python.org/3/reference/datamodel.html#special-method-names




#
