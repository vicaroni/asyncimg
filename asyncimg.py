import asyncio
from re import findall

import aiohttp

urls = [
'https://www.evonove.it',
'http://www.moto.it',
'https://it.wikipedia.org/wiki/Immagine',
'https://pixabay.com',
'https://www.shutterstock.com',
]

async def img_urls(url):
    imgs = []
    async with aiohttp.ClientSession() as client:
        async with client.get(url) as resp:
            imgs = findall('\<img[^\<\>]+src="([^\"]*)', await resp.text())
    print(url)
    for img in imgs:
        print('\t'+img)

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(img_urls(url)) for url in urls]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
