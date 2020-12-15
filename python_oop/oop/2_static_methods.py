

class Person:
    def hello(self):
        print('Hello')

    @staticmethod  # если не требуется доступ к экземпляру класса
    def goodbye():
        print('Goodbye')


# p = Person()
# p.goodbye()
a = Person()
b = Person()
