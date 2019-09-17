from src.modules.dao import Dao
from src.common import KEYS, STRINGS
from src.modules.utilities import is_empty, peek
from src.model.response import GetPersonDetailsResponse, GetPersonMovieCreditsResponse

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

    def is_valid(record):
        return record[KEYS.DEPARTMENT] == STRINGS.DIRECTING and record[KEYS.RELEASE_DATE] != ''

    movie_credits = movie_credits[STRINGS.CREW]

    return (set(record) for record in sorted(movie_credits, key=sort) if is_valid(record))


class Director:

    def __init__(self, name):
        self.name       = name
        self.id         = self._get_director_id()
        self.movies     = self._get_director_movies()

    def _get_director_id(self):
        if is_empty(self.name):
            message = "Director name cannot be empty"
            logging.error(message); print(message)

            return None

        person_details       = self._get_person_details()

        if not is_empty(person_details):
            return str(person_details[KEYS.ID])
        else:
            message = f"Cannot get director id for {self.name}"
            logging.error(message); print(message)
            return None

    def _get_director_movies(self):
        if is_empty(self.id):
            return None

        person_movie_credits = self._get_person_movie_credits()
        movies               = filter_movies_from_credits(person_movie_credits)

        if not is_empty(peek(movies)):
            return movies
        else:
            message = f"Cannot find any movies directed by {self.name} with id: {self.id}"
            logging.error(message); print(message)
            return None

    def _get_person_details(self):
        return GetPersonDetailsResponse(dao.get_person_details(self.name)).get_instance()

    def _get_person_movie_credits(self):
        return GetPersonMovieCreditsResponse(dao.get_person_movie_credits(self.id)).get_instance()

    def list_movies(self):
        if not is_empty(self.movies):
            print(f"List of movies directed by {self.name} \n")

            for movie in self.movies:
                print(movie)
        else:
            message = f"Cannot find any movies directed by {self.name}"
            logging.error(message); print(message)
