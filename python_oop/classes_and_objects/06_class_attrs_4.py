from random import randint, choice


class Lemming:
    total, names = 0, ['Peter', 'Anna', 'Nik', 'Sofi', 'Denn', 'Lora', 'Bred', ]
    names_count = len(names)
    some_text = 'Brrrr, hhhhrhhr ...'
    some_var = some_text + names[-1]

    def __init__(self):
        Lemming.total += 1
        self.name = choice(Lemming.names)

    def __str__(self):
        return 'Leming ' + self.name

    def check_class_attrs(self):
        print('Lemming.total', Lemming.total)
        print('Lemming.names', Lemming.names)
        print('Lemming.names_count', Lemming.names_count)
        print('Lemming.some_text', Lemming.some_text)
        print('Lemming.some_var', Lemming.some_var)

new_lemming = Lemming()
new_lemming.check_class_attrs()
print(new_lemming)
