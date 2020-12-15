top_friends = ['Jose', 'Rolf', 'Anna']

# print(f'My top 1 friend is {top_friends[0]}.')

for i in range(3):
    print(f'My top {i+1} friend is {top_friends[i]}.')

for friend in top_friends:
    print(f'{friend} is one of my top friends.')

for i, friend in enumerate(top_friends):
    print(f'My top {i+1} friend is {friend}')

friend_g = enumerate(top_friends)
print(next(friend_g))  # (0, 'Jose')
k, v = next(friend_g)
print(k)  # 1
print(v)  # Rolf

