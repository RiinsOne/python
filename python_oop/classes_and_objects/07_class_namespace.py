from random import randint, choice


class Lemming:
    names = ['Peter', 'Anna', 'Nik', 'Sofi', 'Denn', 'Lora', 'Bred', ]
    tail_length = 20

    def __init__(self):
        self.tail_length = randint(15, 25)  # атрибут объекта, перекрывает атрибут класса
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Leming ' + self.name + ' with tail ' + str(self.tail_length)


print(Lemming.tail_length)

new_lemming = Lemming()
print(new_lemming.tail_length)
print(new_lemming)
