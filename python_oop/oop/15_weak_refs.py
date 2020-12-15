from weakref import WeakKeyDictionary


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, obj):
#         return isinstance(obj, Person) and self.name == obj.name
#
#     def __hash__(self):
#         return hash(self.name)
#
#
# p = Person('Riin')


class IntDescriptor:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __set__(self, instance, value):
        # print('I got {}'.format(value))
        self._values[instance] = value

    def __get__(self, instance, owner):
        if instance is None:
        #     print('Call from a class')
            return self
        # print('Call from instance')
        return self._values.get(instance)


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()
