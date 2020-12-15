def starts_wit_r(friend):
    return friend.startswith('R')


friends = ['Rolf', 'Jose', 'Randy', 'Anna', 'Mary']
start_with_r = filter(starts_wit_r, friends)  # arg 1: function that returns True/False

# print(next(start_with_r))  # Rolf
# print(list(start_with_r))  # ['Rolf', 'Randy']
# print(list(start_with_r))  # []

start_with_r_2 = filter(lambda x: x.startswith('R'), friends)  # the same

another_starts_with_r = (f for f in friends if f.startswith('R'))  # this perform better
print(another_starts_with_r)  # <generator object <genexpr> at 0x00D39DF0>


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


start_with_r_3 = my_custom_filter(lambda a: a.startswith('R'), friends)
