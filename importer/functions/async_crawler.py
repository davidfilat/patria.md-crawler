import asyncio

from bs4 import BeautifulSoup

import aiohttp
import pushover

from .process_movie_info import get_available_info, get_upcoming_info

CONCURRENCY = 8
TIMEOUT = 600
pushover.init("a8x1dg2jk8kmtepef5zdtfnbsvvmmy")
PUSHOVER = pushover.Client("ug5eogk24pdq36nqacu8anur4r4js9")


async def fetch(session, sem, url, type_):
    try:
        async with sem:
            headers = {"User-Agent": "Google Spider"}
            async with session.get(url, headers=headers) as response:
                text = await response.read()
                soup = BeautifulSoup(text.decode("utf-8"), "html5lib")
                if type_ == "upcoming":
                    result = get_upcoming_info(soup)
                else:
                    result = get_available_info(soup)
                    result["url"] = url
            return result

    except Exception:
        PUSHOVER.send_message(
            str(url + "\n" + str(url)), title="Patria importer error!"
        )


async def get_movies_data(urls, type_):
    sem = asyncio.Semaphore(CONCURRENCY)
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *(asyncio.wait_for(fetch(session, sem, i, type_), TIMEOUT) for i in urls)
        )
    return results


def get_movies_info(urls, type_="available"):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(get_movies_data(urls, type_))
    data = loop.run_until_complete(future)

    return data


if __name__ == "__main__":
    urls = [
        "https://patria.md/movies/spionul-care-mi-a-dat-papucii/",
        "https://patria.md/movies/predatorul/",
    ]
    get_movies_info(urls)
