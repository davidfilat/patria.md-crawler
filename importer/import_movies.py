from .functions.async_crawler import get_movies_info
from .functions import get_movies_urls
import json
import pushover
pushover.init("a8x1dg2jk8kmtepef5zdtfnbsvvmmy")
PUSHOVER = pushover.Client("ug5eogk24pdq36nqacu8anur4r4js9")


def available():
    return get_movies_info(get_movies_urls.available())


def upcoming():
    return get_movies_info(get_movies_urls.upcoming(), type_='upcoming')


def import_all(filename='data.json', save=False):
    available_list = available()
    upcoming_list = upcoming()
    data = {
        "available": available_list,
        "upcoming": upcoming_list
    }
    if save == True:
        with open(filename, 'w') as f:
            f.write(json.dumps(data))

    PUSHOVER.send_message(
        str('Felicitări, import complete'), title="Patria importer complete!")

    return data


if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()
    data = import_all()
    pp.pprint(data['available'])
    print('-------------------------------------')
    print('-------------------------------------')
    print('-------------------------------------')
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data['upcoming'])
