from bs4 import BeautifulSoup
def get_title(soup):
    title = soup.title.string.strip()
    ri = title.find('|') 
    title = title[:ri].strip()
    return title

deg get_release_date(soup):
    release_date = soup.select_one(".premiere > span").next_sibling.strip()
    return release_date


filename = "output.html"
with open(filename, "r") as f:
    soup = BeautifulSoup(f, 'html.parser')
    print(get_title(soup))
    print(get_release_date(soup))


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