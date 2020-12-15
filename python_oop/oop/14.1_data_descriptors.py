from time import time
import ctypes


def ref_count(obj_id):
    return ctypes.c_long.from_address(obj_id).value


class IntDescriptor:
    def __init__(self):
        self._values = {}

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


# v1 = Vector()
# v2 = Vector()
