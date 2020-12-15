class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __add__(self, other):
        new_obj = Backpack()
        new_obj.content.extend(self.content)
        if isinstance(other, Backpack):
            new_obj.content.extend(other.content)
        else:
            new_obj.content.extend(other)
        return new_obj

    def __iadd__(self, other):
        self.content.extend(other.content)
        return self


my_bp = Backpack('sandwich')
son_bp = Backpack('banana')
# new_bp = my_bp + son_bp
new_bp = my_bp + ['apple', 'orange']  # Backpack: sandwich, apple, orange
# new_bp = my_bp + 'apple'  # Backpack: sandwich, a, p, p, l, e
print(new_bp)
my_bp += son_bp
print(my_bp)  # Backpack: sandwich, banana
