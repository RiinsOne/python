

# class Person:
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#         self._full_name = None
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         self._name = value
#         self._full_name = None
#
#     @property
#     def surname(self):
#         return self._name
#
#     @surname.setter
#     def surname(self, value):
#         self._surname = value
#         self._full_name = None


class StringD:
    def __init__(self, value=None):
        if value:
            self.set(value)

    def set(self, value):
        self._value = value

    def get(self):
        return self._value


class Person:
    def __init__(self, name, surname):
        self.name = StringD(name)
        self.surname = StringD(surname)


p = Person('OG', 'Riins')
