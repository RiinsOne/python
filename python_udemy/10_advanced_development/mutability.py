friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))  # random number 9922768

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

print(id(friends_last_seen))  # 9464064

friends_last_seen['Rolf'] = 0  # friends_last_seen.__setitem__()

print(id(friends_last_seen))  # 9464064

my_int = 5
my_int = my_int + 1  # my_int.__add__(self, 1): return self.value + 1
my_int += 1  # my_int.__iadd__(self, 1)


"""
integers -> all functions return event_more_view int objects
floats
strings
tuples
"""

"""
"""
