class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        self.content.append(item)
        print('Put to the backpack:', item)

    def inspect(self, ):
        print('Items in the backpack:')
        for item in self.content:
            print('-----', item)

    def __del__(self):
        self.content = None
        print('Bye...')


my_backpack = Backpack(gift='flashcard')
my_backpack.add('laptop')
my_backpack.add(item='acc charge for a laptop')
my_backpack.inspect()
