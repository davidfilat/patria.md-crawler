from async_crawler import get_movies_info
import get_movies_urls as movies
import pprint
pp = pprint.PrettyPrinter()
available = get_movies_info(movies.available())
upcoming = get_movies_info(movies.upcoming(), type_='upcoming')

pp.pprint(available)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(upcoming)
