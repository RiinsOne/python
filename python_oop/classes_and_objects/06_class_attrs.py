from random import randint


class Lemming:
    pass


total_lemmings = 0
lemming_1 = Lemming()
total_lemmings += 1
lemming_2 = Lemming()
total_lemmings += 1
lemming_3 = Lemming()
total_lemmings += 1

family = []
family_size = randint(16, 32)
while len(family) < family_size:
    new_lemming = Lemming()
    family.append(new_lemming)
    total_lemmings += 1
print(total_lemmings)
