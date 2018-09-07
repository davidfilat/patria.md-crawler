from bs4 import BeautifulSoup
import requests


def get_title(soup):
    title = soup.title.string.strip()
    ri = title.find('|')
    title = title[:ri].strip()
    return title


def get_release_date(soup):
    release_date = soup.select_one(".premiere > span").next_sibling.strip()
    return release_date


def get_schedule(soup):
    previous_cinema = ''
    schedules_soup = soup.select('.cinema')
    schedules_dict = []
    for schedule in schedules_soup:
        schedule = schedule.parent
        if schedule.select_one('.time').text.strip() == 'timpul':
            continue

        if schedule.select_one('.cinema > span') == None:
            cinema = previous_cinema
        else:
            cinema = schedule.select_one('.cinema > span').text.strip()
            previous_cinema = cinema
        halls = [item.text.strip() for item in schedule.select('.hall')]
        times = [item.text.strip() for item in schedule.select('.time')]
        schedule_1 = {'cinema': cinema}
        schedule_1['schedule'] = {}
        for i in range(0, len(halls)):
            schedule_1['schedule'][halls[i]] = times[i]
        schedules_dict.append(schedule_1)
    return schedules_dict


# filename = "output.html"
# with open(filename, "r") as f:
url = 'https://patria.md/movies/spionul-care-mi-a-dat-papucii/'
r = requests.get(url)
if r.status_code >= 200:
    soup = soup = BeautifulSoup(r.text, 'html.parser')
    print(get_title(soup))
    print(get_release_date(soup))
    print(get_schedule(soup))
