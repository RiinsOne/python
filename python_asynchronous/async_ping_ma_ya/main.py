import subprocess as sp
import asyncio


async def my(url):
    for num, _ in enumerate(range(1, 11), 1):
        sp1 = sp.Popen('ping -n 1 {} | FIND "Ответ"'.format(url), shell=True, stdout=sp.PIPE)
        out = sp1.stdout.read().decode('cp866')
        print(num, url, out)
        await asyncio.sleep(1)

# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(my('mail.ru')),
#     asyncio.ensure_future(my('ya.ru')),
# ]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

async def main():
    await asyncio.gather(my('mail.ru'), my('ya.ru'))


if __name__ == '__main__':
    asyncio.run(main())
