import asyncio
import time


def clock(name, repeats):
    for r in range(repeats):
        strf_time = time.strftime('%X')
        print("Clock {name} shows time: {strf_time}".format(name=name, strf_time=strf_time))
        time.sleep(1)

# clock('One', 5)


def main():
    clock('One', 3)
    clock('Two', 4)
    clock('Three', 5)


main()
