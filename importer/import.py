from async_crawler import get_movies_info
import get_movies_urls as movies


def available():
    return get_movies_info(movies.available())


def upcoming():
    return get_movies_info(movies.upcoming(), type_='upcoming')


if __name__ == "__main__":
    import pprint
    pp = pprint.PrettyPrinter()
    available_list = get_movies_info(movies.available())
    upcoming_list = get_movies_info(movies.upcoming(), type_='upcoming')

    pp.pprint(available_list)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(upcoming_list)
