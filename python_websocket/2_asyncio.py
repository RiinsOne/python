# bad example

import asyncio
import random


async def task(pid_num):
    """
    Some non-deterministic task
    """
    await asyncio.sleep(random.randint(1, 5))
    print('Task {pid} done'.format(pid=pid_num))


# def sync_func():
#     for pid in range(1, 10):
#         task(pid)


# async def async_func():
#     for pid in range(1, 10):
#         await task(pid)


# print('Synchronous:')
# sync_func()

print('Asynchronous:')
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(task(pid)) for pid in range(10)]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
