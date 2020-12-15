from ogframework import newline

rabbits = 3
while rabbits > 0:
    print(rabbits, end=' ')  # 3 2 1
    rabbits -= 1

newline()
while True:
    text = input('Type any number or stop/exit to quit: ')
    if text == 'stop' or text == 'exit':
        print('Exiting the program. Bye!')
        break
    elif text.isdigit():
        print(f'The number is {text}.')
    else:
        print('What is it?')


#
