from src.modules.dao import Dao
from src.common import KEYS, STRINGS
from src.modules.utilities import is_empty, peek
from src.model.person import Person

import logging

# Initialize Dao
dao = Dao()


def filter_movies_from_credits(movie_credits):
    """
    This function filters movies based on the filter criteria
    :param movie_credits:
    :return: filtered movies generator object
    """
    def set(record):
        return 'Release date: {0[release_date]} Title: {0[title]}'.format(record)

    def sort(record):
        return record[KEYS.RELEASE_DATE]

    def condition(record):
        return record[KEYS.DEPARTMENT] == STRINGS.DIRECTING and record[KEYS.RELEASE_DATE] != ''

    movie_credits = movie_credits[STRINGS.CREW]

    return (set(record) for record in sorted(movie_credits, key=sort) if condition(record))


class Director(Person):

    def __init__(self, name):
        super().__init__(name)

        self.movies             = self._get_director_movies()

    def _get_director_movies(self):
        if is_empty(self.get_id()):
            return None

        movies               = filter_movies_from_credits(self.get_movie_credits())

        if not is_empty(peek(movies)):
            return movies
        else:
            message = f"Cannot find any movies directed by {self.name}"
            logging.error(message); print(message)
            return None

    def list_movies(self):
        if not is_empty(self.movies):
            print(f"List of movies directed by {self.name} \n")

            for movie in self.movies:
                print(movie)
        else:
            message = f"Cannot find any movies directed by {self.name}"
            logging.error(message); print(message)
