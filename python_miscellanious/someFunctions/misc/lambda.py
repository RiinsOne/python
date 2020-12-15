from ogframework import newline


def edit_story(words, func):
    for word in words:
        print(func(word))


s = ['aaa', 'bbb', 'ccc']  # создали список
def f(word):
    return word.capitalize() + '!'

edit_story(s, f)

newline()
edit_story(s, lambda x: x.capitalize() + '!')
# lambda line: line.capitalize() + '!'
# lambda переменная: после return, но сам return не пишится


