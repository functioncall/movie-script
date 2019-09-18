from src.modules.dao import Dao
from src.modules.utilities import is_empty
from src.model.response import GetPersonDetailsResponse, GetPersonMovieCreditsResponse

import logging

# Initialize Dao
dao = Dao()


class Person:

    def __init__(self, name):
        self.name          = name
        self.data          = self._get_person_details()
        self.id            = self._get_person_id()
        self.movie_credits = self._get_person_movie_credits()

    def get_id(self):
        return self.id

    def get_movie_credits(self):
        return self.movie_credits

    def _get_person_details(self):
        if self._is_name_empty():
            return None
        return GetPersonDetailsResponse(dao.get_person_details(self.name))

    def _get_person_id(self):
        if is_empty(self.data):
            return None

        return self.data.id

    def _get_person_movie_credits(self):
        if is_empty(self.id):
            return None

        return GetPersonMovieCreditsResponse(dao.get_person_movie_credits(self.id)).movie_credits

    def _is_name_empty(self):
        if is_empty(self.name):
            message = "Person name cannot be empty"
            logging.error(message);
            print(message)

            return True

