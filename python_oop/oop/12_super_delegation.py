#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#
# class Student(Person):
#     def __init__(self, name, surname):
#         super().__init__(name)
#         self.surname = surname


class  Person:
    def hello(self):
        print('Bound with {}'.format(self))


class Student(Person):
    def hello(sefl):
        print('Student obj.hello() is called')
        super().hello()


s = Student()
