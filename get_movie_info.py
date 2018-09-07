import requests

from bs4 import BeautifulSoup
import get_movies_urls as get_movies

available_urls = get_movies.in_the_theatre()

for url in available_urls:
    r = requests.get(url)
    if r.status_code >= 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup.title.string)
        release_dates = soup.select(".premiere > span")
        for date in release_dates:
            release_date = date.next_sibling.strip()
            print(release_date)
        # tables = soup.find_all('tbody')
        # for table in tables:
        #     rows = table.find_all('tr')
        #     previous_cinema = None
        rows = soup.select('.cinema span')
        cinemas = []
        previous_cinema = None
        for cinema in rows:
            # cinema = row.select_one('.cinema > span')
            if cinema == None:
                cinemas.append(previous_cinema)
            else:
                cinemas.append(cinema.text)
            previous_cinema = cinema

            print(cinemas)
f