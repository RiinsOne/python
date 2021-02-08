from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@timeit
def make_one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l


@timeit
def make_two(n):
    l = [x for x in range(n) if x % 2 == 0]
    return l


# l1 = make_one(10**6)
# l2 = make_two(10**6)


# l1 = timeit(make_one)
# print(type(l1), l1.__name__)  # <class 'function'> wrapper
# a = l1(10)

# l1 = timeit(make_one)(10)  # => wrapper(10)


def timeit_2(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@timeit_2('name')
def make_it(n):
    return n + n

print(make_it(10))

n1 = timeit_2('name')(make_it)(10)  # тоже самое, что и @timeit_2
