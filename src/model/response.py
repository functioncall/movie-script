from src.modules.utilities import json_parser, is_empty
from src.common import KEYS

import logging


class Response:
    """
    Abstract class to handle api response
    """
    def parse_response(self):
        """
        Abstract method to implement parsing logic
        :return:
        """
        pass


class GetPersonDetailsResponse(Response):
    """
    This class handles get person details response data
    """
    def __init__(self, data):
        self.name  = data['person_name']
        self.data  = data['result']
        self._data = self.parse_response()
        self.id    = self.get_person_id()

    def parse_response(self):
        if not is_empty(self.data):
            result = json_parser(self.data.content)['results']

            if not result:
                return None
            else:
                return result[0]
        #                     ^
        #              We select the first (best) match out of list of people
        #              matching the search query
        else:
            return None

    def get_person_id(self):

        if not is_empty(self._data):
            return str(self._data[KEYS.ID])
        else:
            message = f"Cannot get Id for {self.name}"
            logging.error(message); print(message)
            return None


class GetPersonMovieCreditsResponse(Response):
    """
    This class handles get person movie credits response data
    """
    def __init__(self, data):
        self.data = data
        self._data = self.parse_response()
        self.movie_credits = self._data

    def parse_response(self):
        if not is_empty(self.data):
            result = json_parser(self.data.content)

            if not result:
                return None
            else:
                return result
        else:
            return None
