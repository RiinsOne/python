import asyncio
import time


RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'


async def clock(name, repeats, color):
    for r in range(repeats):
        strf_time = time.strftime('%X')
        print("{color} Clock {name} shows time: {strf_time}".format(color=color ,name=name, strf_time=strf_time))
        await asyncio.sleep(1)

# clock('One', 5)


async def main():
    await asyncio.gather(
    clock('One', 7, RED),
    clock('Two', 8, GREEN),
    clock('Three', 9, YELLOW),
    )


asyncio.run(main())
