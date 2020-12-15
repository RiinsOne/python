from random import randint, choice


class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Denn', 'Lora', 'Bred', ]
    total = 0
    tail_length = 20

    def __init__(self):
        self.tail_length = randint(15, 25)
        self.name = choice(Lemming.names)
        Lemming.total = Lemming.total + 1

    def __str__(self):
        return 'Leming ' + self.name + ' with tail ' + str(self.tail_length)


burrow = []
burrow_depth = randint(90, 100)
while len(burrow) < burrow_depth:
    family = []
    family_size = randint(16, 32)
    while len(family) < family_size:
        new_lemming = Lemming()
        family.append(new_lemming)
    burrow.append(family)
print(Lemming.total)
print(len(burrow))
