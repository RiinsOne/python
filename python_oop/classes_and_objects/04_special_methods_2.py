class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print('Put to the backpack:', item)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __bool__(self):
        return self.content != []

    def __len__(self):
        return len(self.content)


my_bp = Backpack()
my_bp.add('laptop')
# print(bool(my_bp), len(my_bp))
if my_bp:
    print('Backpack isn\'t empty')
    print('There are:', len(my_bp), 'items')
else:
    print('Backpack is empty')

# by default all objects are True
