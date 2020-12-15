def bold(func):
    def inner(who):
        print('<b>')
        func(who)
        print('</b>')
    return inner


def italic(func):
    def inner(who):
        print('<i>')
        func(who)
        print('</i>')
    return inner


@italic
@bold
def hello(who):
    print(f'Hello {who}')


hello('OG')
# <i>
# <b>
# Hello OG
# </b>
# </i>

#
