from time import sleep, time
import asyncio


async def spider(site_name):
    for page in range(1, 4):
        # sleep(1)  # блокирующая функция
        await asyncio.sleep(1)
        print(site_name, page)


start = time()

spiders = [
    asyncio.ensure_future(spider('Blog')),
    asyncio.ensure_future(spider('News')),
    asyncio.ensure_future(spider('Forum')),
]

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(asyncio.gather(*spiders))
event_loop.close()

print(time() - start)
