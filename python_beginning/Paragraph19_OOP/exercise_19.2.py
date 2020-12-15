class Animal:
    name = ''

    def __init__(self, newName):
        self.name = newName
        print(f'Родилось животное {newName}')

    def eat(self):
        print('Ням-ням')

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def makeNoise(self):
        print(f'{self.name} говорит Гррр')


newAnimal = Animal('Didier')  # Родилось животное Didier
print(newAnimal.getName())  # Didier
newAnimal.setName('Timka')
newAnimal.eat()  # Ням-ням
newAnimal.makeNoise()  # Timka говорит Гррр

#
