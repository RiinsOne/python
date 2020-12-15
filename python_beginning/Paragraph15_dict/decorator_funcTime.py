import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        print(t)
        res = f(*args, **kwargs)
        print('Время выполнения функции: %f' % (time.time()-t))
        return res
    return tmp


# декоратор, выполняющий задержку переданной функции на 2 секунды
def pause(f):
    def tmp(*args, **kwargs):
        time.sleep(2)  # задержка на 2 секунды
        return f(*args, **kwargs)
    return tmp


@timer
@pause
def func(x, y):
    return x + y


func(1, 4)  # Время выполнения функции: 1.000635
#
