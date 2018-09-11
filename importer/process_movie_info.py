import re


def get_title(soup):
    title = soup.title.string.strip()
    ri = title.find('|')
    title = title[:ri].strip()
    return title


def get_release_date(soup):
    release_date = soup.select_one(".premiere > span").next_sibling.strip()
    return release_date


def get_duration(soup):
    try:
        duration = soup.select_one('.duration').text
        return int(duration[:duration.find('min')].strip())
    except:
        return None


def get_schedule(soup):
    previous_schedule = None
    schedules_soup = soup.select('.cinema')
    schedules_dict = []
    for schedule_soup in schedules_soup:
        schedule_soup = schedule_soup.parent
        if schedule_soup.select_one('.time').text.strip() == 'timpul':
            continue

        elif schedule_soup.select_one('.cinema > span') == None:
            schedule = previous_schedule
            schedule['schedule'].append(
                [schedule_soup.select_one('.hall').text.strip(), schedule_soup.select_one('.time').text.strip()])

        else:
            cinema = schedule_soup.select_one('.cinema > span').text.strip()
            hall = schedule_soup.select_one('.hall').text.strip()
            time = schedule_soup.select_one('.time').text.strip()
            schedule = {'cinema': cinema}
            schedule['schedule'] = []
            schedule['schedule'].append([hall, time])

            previous_schedule = schedule
            schedules_dict.append(schedule)
    return schedules_dict


def get_image(soup):
    p = re.compile('(.*)-...x...(.*)')
    image = soup.select_one('.attachment-movie-thumb-big')['src']
    m = re.match(p, image)
    return ''.join(m.groups())

def get_trailer_embed(soup):
    return soup.select_one('.trailer iframe')['src']


def get_trailer_link(soup):
    p = re.compile('(.*)\/embed\/(.*)')
    link = soup.select_one('.trailer iframe')['src']
    m = re.match(p, link)
    return '/watch?v='.join(m.groups())


def get_available_info(soup):
    return {
        'title': get_title(soup),
        'release_date': get_release_date(soup),
        'schedule': get_schedule(soup),
        'duration': get_duration(soup),
        'image': get_image(soup),
        'trailer': get_trailer_link(soup),
        'trailer_embed': get_trailer_embed(soup)
    }


def get_upcoming_info(soup):
    return {
        'title': get_title(soup),
        'release_date': get_release_date(soup),
        'image': get_image(soup),
        'trailer': get_trailer_link(soup),
        'trailer_embed': get_trailer_embed(soup)
    }


if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    # filename = "output.html"
    # with open(filename, "r") as f:
    # url = 'https://patria.md/movies/spionul-care-mi-a-dat-papucii/'
    url = "http://patria.md/movies/meg-confruntare-in-adancuri/"
    r = requests.get(url)
    if r.status_code >= 200:
        soup = soup = BeautifulSoup(r.text, 'html.parser')
        pp.pprint(get_available_info(soup))
