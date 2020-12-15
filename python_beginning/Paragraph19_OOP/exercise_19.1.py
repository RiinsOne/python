class Cat():
    name = ''
    color = ''
    weight = 0

    def meow(self):
        print(f'{self.name} meow, meow..')


myCat = Cat()
myCat.name = 'Kitty'
myCat.color = 'Black'
myCat.weight = 5

myCat.meow()
Cat.meow(myCat)

#
