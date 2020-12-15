class Ddd():
    def __init__(self, input_name):
        self.hidden_name = input_name  # атрибут hidden_name

    def get_name(self):
        print('внутри getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('внутри setter')
        self.hidden_name = input_name

    # методы get_name и set_name - свойства атрибута name
    # через name обращаемся к hidden_name
    name = property(get_name,set_name)


# создание объекта класса Ddd
f = Ddd('total_handicap')
# обращение к атрибуту name приведет к вызову метода get_name()
print(f.name)  # внутри getter\n total_handicap
print(f.get_name())  # внутри getter\n total_handicap

print()
# установка знаения атрибута name приведет к вызову метода set_name()
f.name = 'OG'
print(f.name)  # внутри setter\n внутри getter\n OG
f.set_name('OG OG')
print(f.name)  # внутри setter\n внутри getter\n OG OG


















#