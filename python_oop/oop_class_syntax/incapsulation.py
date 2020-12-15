class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_descr(self):
        # self._d - приватный атрибут
        self._d = self.b ** 2 - 4 * self.a * self.c

    def get_desc(self):
        return self._d

    def calc_root(self, order=1):
        if order == 1:
            x = (-self.b + self._d ** (1 / 2.0)) / 2 * self.a
        else:
            x = (-self.b - self._d ** (1 / 2.0)) / 2 * self.a
        return x


class A:
    def __init__(self):
        self.a = 1
        self._b = 10
        self.__d = 20  # супер приватная переменная

    def set_c(self, c):
        self._c = int(c)

    def calc_b(self):
        self._b += self.a

    def get_b(self):
        return self._b

    def __len__(self):
        return self.__d


a = A()
print(a.a)  # 1
print(a._b)  # 10
a._b = 20  # изменять можно, но не надо, т.к. приватный атрибут

print(a.get_b())  # 20

a.calc_b()  # увеличить b на значение a
print(a.get_b())  # 21

print()
a.set_c('2')
print(a._c)  # 2

print()
print(a._A__d)  # 20
a._A__d = 30
print(a._A__d)  # 30

print(dir(a))

print(len(a))  # 30

#
