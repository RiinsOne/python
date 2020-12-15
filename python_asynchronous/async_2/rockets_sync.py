import time
import random


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


if __name__ == '__main__':
    rockets_count = len(rockets())
    for delay, countdown in rockets():
        launch_rocket(delay, countdown)
        rockets_count -= 1
        print('{} rockets left...'.format(rockets_count))
