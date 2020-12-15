import time
import random
from threading import Thread


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print("{}...".format(i + 1))
        time.sleep(0.2)
    print("Rocket launched")


def rockets():
    N = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(N)
    ]


def run_threads():
    threads = [
        Thread(target=launch_rocket, args=(delay, countdown))
        for delay, countdown in rockets()
    ]
    for t in threads:
        t.start()
    for t in treads:
        t.join()


if __name__ == '__main__':
    run_threads()
