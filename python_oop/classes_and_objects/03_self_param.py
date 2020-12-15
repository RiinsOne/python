class Backpack:

    def add(self, item):
        print('Put in backpack ', item)
        self.content = item


my_backpack = Backpack()
my_backpack.add(item='laptop')

my_son_backpack = Backpack()
my_son_backpack.add(item='book')

print(my_son_backpack.content)

# my_backpack.add(item='laptop')  # через инстанс self не нужен
# Backpack.add(self=my_backpack, item='laptop')  # через class нужен self
