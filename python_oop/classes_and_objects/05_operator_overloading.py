class Backpack:

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def __str__(self):
        return 'Backpack: ' + ', '.join(self.content)

    def __eq__(self, other):
        return self.content == other.content


my_bp = Backpack(gift='sandwich')
son_bp = Backpack(gift='sandwich')

if my_bp == son_bp:
    print('How similar we are...')

if Backpack.__eq__(self=my_bp, other=son_bp):
    print('How similar we are...')
