def get_parameter(name):
    while True:
        p = input(f'Enter the parameter of the equation: {name} = ')
        if p.replace('.', '').isdigit() and float(p) != 0:
            p = float(p)
            return p
        else:
            print('Please enter the number of nonzero!')


class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_descr(self):
        self.d = self.b ** 2 - 4 * self.a * self.c

    def get_desc(self):
        return self.d

    def calc_root(self, order=1):
        if order == 1:
            x = (-self.b + self.d ** (1 / 2.0)) / 2 * self.a
        else:
            x = (-self.b - self.d ** (1 / 2.0)) / 2 * self.a
        return x

#
