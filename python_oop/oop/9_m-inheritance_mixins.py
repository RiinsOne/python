

class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food should be set')
        print('I like {}'.format(self.food))


class Person:
    def hello(self):
        print('I am Person')


class Student(FoodMixin, Person):
    food = 'Pizza'
    
    def hello(self):
        print('I am Student')


s = Student()
