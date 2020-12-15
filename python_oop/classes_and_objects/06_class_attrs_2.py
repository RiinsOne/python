from random import randint


class Lemming:
    total = 0

    def __init__(self):
        Lemming.total += 1


family = []
family_size = randint(16, 32)
while len(family) < family_size:
    new_lemming = Lemming()
    family.append(new_lemming)
print(Lemming.total)
