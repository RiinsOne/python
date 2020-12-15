class Backpack:

    def __init__(self):
        self.content = []

    def add(self, item):
        self.content.append(item)
        print('Put to the backpack:', item)

    def inspect(self):
        print('Items in the backpack:')
        for item in self.content:
            print('-----', item)


my_backpack = Backpack()
my_backpack.add(item='laptop')
my_backpack.add(item='acc charge for a laptop')
my_backpack.inspect()

print('-----')


class BackpackTwo:

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print('Put to the backpack:', item)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)


my_bp_two = BackpackTwo('mobile')
my_bp_two.add('laptop')
my_bp_two.add('acc charge for a laptop')
print(str(my_bp_two))
print(my_bp_two)
print(my_bp_two.__str__())  # Backpack: mobile, laptop, acc charge for a laptop

# __len__ - get length of a object with len()
# __hash__ - get unique object hash with hash() or for some operations with hash collections - sets and dicts
#__bool__ - calling to receive "boolean" of a object with bool()
