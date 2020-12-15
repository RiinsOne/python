friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}


def see_friend(friends, name):
    # print(id(friends))
    # print(friends is friends_last_seen)  # True
    friends[name] = 0


# print(id(friends_last_seen))  # 38627536
see_friend(friends_last_seen, 'Rolf')  # 38627536
# print(id(friends_last_seen))  # 38627536


age = 20


def increase_age(current_age):
    current_age = current_age + 1


print(id(age))  # 1530714592
increase_age(age)
print(id(age))  # 1530714592


primes = [2, 3, 5]

print(id(primes))  # 22824400

primes += [7, 11]  # primes = primes.__iadd__([7, 11])
# в основной список добавляются элементы
print(id(primes))  # 22824400

primes = [2, 3, 5] + [7, 11]  # primes = primes.__add__([7, 11])
# создается новый список
print(id(primes))  # 49894064
