

class Person:
    def hello(self):
        print('I am Person')


class Student(Person):
    # def hello(self):
    #     print('I am Student')

    def goodbye(self):
        print('goodbye')


s = Student()


class PersonOne:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')


class StudentOne(PersonOne):
    pass


s1 = StudentOne('Riins')
