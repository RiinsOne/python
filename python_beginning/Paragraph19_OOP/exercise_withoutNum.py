class Animal:
    def __init__(self, newName=''):
        self.name = newName
        print(f'An animal was born')

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def eat(self):
        print('Yum-yum')

    def makeNoise(self):
        print(f'{self.name} growls Grrrrr')


newAnimal = Animal('Didier')
print(newAnimal.getName())
print()


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('A cat was born')

    def makeNoise(self):
        print(f'{self.name} says Meow')


newCat = Cat()  # An animal was born\n A cat was born
newCat.setName('Kitty')
print(newCat.getName())  # Kitty
newCat.makeNoise()  # Kitty says Meow
newCat.eat()  # Yum-yum
print()


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('A dog was born')

    def makeNoise(self):
        print(f'{self.name} says Woof')


newDog = Dog()
# An animal was born
# A dog was born

newDog.setName('Didier')
newDog.makeNoise()  # Didier says Woof
print()
print()


kitty = Cat()
kitty.setName('Kitty')
kitty.eat()
kitty.makeNoise()
print()

fstDog = Dog()
fstDog.setName('Timka')
fstDog.eat()
fstDog.makeNoise()
print()

splAnimal = Animal()
splAnimal.setName('Didier')
splAnimal.eat()
splAnimal.makeNoise()












#
