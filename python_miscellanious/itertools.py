import itertools, time

def get_iter(seconds, start, step):
    iter = itertools.count(start=start, step=step)
    sum = start
    while sum > 0 and sum < 100:
        next_iter = next(iter)
        sum += step
        print('sum is: ', sum)
        print(next_iter)
        time.sleep(seconds)

get_iter(1, 56, -16)
