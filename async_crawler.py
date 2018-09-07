import asyncio
from bs4 import BeautifulSoup
import aiohttp
import validators
import html5lib

CONCURRENCY = 8
TIMEOUT = 600


async def fetch(session, sem, url):
    if validators.url(url):
        async with sem:
            headers = {'User-Agent': 'Google Spider'}
            async with session.get(url, headers=headers) as response:
                text = await response.read()
                soup = BeautifulSoup(text.decode('utf-8'), 'html5lib')
                data =
                return
    else:
        return None


async def get_url_data(urls):
    sem = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*(
            asyncio.wait_for(fetch(session, sem, i), TIMEOUT) for i in urls))
    return responses


def crawl(urls):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_url_data(urls))
    data = loop.run_until_complete(future)
    print(data)
    return data


if __name__ == "__main__":
    urls = ['http://cnn.com', 'http://google.com', 'http://twitter.com']
    crawl(urls)
