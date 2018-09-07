import requests
from bs4 import BeautifulSoup

SOUP = None


def crawl():
    global SOUP
    if SOUP:
        pass
    else:
        url = requests.get("https://patria.md/movies/")
        if url.status_code == 200:
            return BeautifulSoup(url.text, 'html.parser')


SOUP = crawl()


def is_coming_soon_movie(css_class):
    return css_class == "coming-soon-mark"


def upcoming(soup=SOUP):
    # global SOUP
    result = []
    movies = soup.find_all(
        class_=is_coming_soon_movie)
    for movie in movies:
        link = movie.find_previous_sibling()
        href = link.get('href')
        result.append(href)
    return result


def all(soup=SOUP):
    # global SOUP
    result = []
    movies = soup.select('.movies-item > figure > a')
    for movie in movies:
        href = movie.get('href')
        result.append(href)
    return result


def available():
    return set(all()) - set(upcoming())


if __name__ == "__main__":
    print(available())
