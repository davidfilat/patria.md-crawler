import asyncio
import aiohttp
from bs4 import BeautifulSoup
from process_movie_info import get_upcoming_info, get_available_info

CONCURRENCY = 8
TIMEOUT = 600


async def fetch(session, sem, url, type_):
    async with sem:
        headers = {'User-Agent': 'Google Spider'}
        async with session.get(url, headers=headers) as response:
            text = await response.read()
        soup = BeautifulSoup(text.decode('utf-8'), 'html5lib')
        if type_ == 'upcoming':
            result = get_upcoming_info(soup)
        else:
            result = get_available_info(soup)
        result['url'] = url
        return result


async def get_movies_data(urls, type_):
    sem = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*(
            asyncio.wait_for(fetch(session, sem, i, type_), TIMEOUT) for i in urls))
    return results


def get_movies_info(urls, type_='available'):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_movies_data(urls, type_))
    data = loop.run_until_complete(future)
    print(data)
    return data


if __name__ == "__main__":
    urls = ['https://patria.md/movies/spionul-care-mi-a-dat-papucii/',
            'https://patria.md/movies/predatorul/']
    get_movies_info(urls)
