from time import time


class Epoch:
    def __get__(self, instance, owner_class):
        # print(f'Self: {self}')
        # print(f'Instance: {instance}')
        # print(f'Owner class: {owner_class}')

        print('id of self: {}'.format(id(self)))

        if instance is None:
            return self
        return int(time())

    def __set__(self, instance, value):
        pass


class MyTime:
    epoch = Epoch()


m = MyTime()
