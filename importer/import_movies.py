import json

import pushover

from .functions import get_movies_urls
from .functions.async_crawler import get_movies_info

pushover.init("a8x1dg2jk8kmtepef5zdtfnbsvvmmy")
PUSHOVER = pushover.Client("ug5eogk24pdq36nqacu8anur4r4js9")


def available():
    """Get the schedule for the available movies at Patria Cinema 
    (data crawled from the official patria.md site).

    Return:
        dict -- a dictionary with the schedule for all upcoming movies, 
        containing title, release_date, image, etc.
    """
    return get_movies_info(get_movies_urls.available())


def upcoming():
    """Get the data for the upcoming movies at Patria Cinema.

    Return:
        dict -- a dictionary with data about all upcoming movies.
    """
    return get_movies_info(get_movies_urls.upcoming(), type_="upcoming")


def import_all(filename="data.json"):
    """Retrieve movie data from patria.md in a dict containing schedule 
    for available movies and data about upcoming movies.
    Keyword Arguments:
        filename {str} -- filename or path to save data for persistance.
            (default: {"data.json"})

    Return:
        dict -- a dictionary containing the schedule for the available movies
                and the data about upcoming movies.
    """
    available_list = available()
    upcoming_list = upcoming()
    data = {"available": available_list, "upcoming": upcoming_list}
    if filename:
        with open(filename, "w") as f:
            f.write(json.dumps(data))

    PUSHOVER.send_message(
        str("Felicitări, import complete"), title="Patria importer complete!"
    )

    return data


if __name__ == "__main__":
    import pprint

    pp = pprint.PrettyPrinter()
    data = import_all()
    pp.pprint(data["available"])
    print("-------------------------------------")
    print("-------------------------------------")
    print("-------------------------------------")
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data["upcoming"])
