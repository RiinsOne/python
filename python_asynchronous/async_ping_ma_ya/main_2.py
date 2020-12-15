import subprocess as sp
import asyncio


async def my(url):
    sp1 = sp.Popen('ping -n 1 {} | FIND "Ответ"'.format(url), shell=True, stdout=sp.PIPE)
    out = sp1.stdout.read().decode('cp866')
    print(url, out)
    await asyncio.sleep(2)


async def main():
    while True:
        await asyncio.gather(my('mail.ru'), my('ya.ru'))


if __name__ == '__main__':
    asyncio.run(main())
