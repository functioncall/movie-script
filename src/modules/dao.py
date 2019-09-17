from src.common import configurations
from src.modules import utilities
from src.common import KEYS, STRINGS
from src.modules.logger import logger
from src.modules.utilities import timer

import requests
from requests.exceptions import RequestException

create_endpoint = utilities.create_endpoint


class Dao:
    """
    Data Access Object class for the movie database api
    """

    def __init__(self):
        endpoints = configurations.configurations.get(KEYS.MOVIE_DB).get(STRINGS.ENDPOINTS)

        self.get_search_person_endpoint             = endpoints.get(KEYS.SEARCH_PERSON_ENDPOINT)
        self.get_person_movie_credits_base_endpoint = endpoints.get(KEYS.PERSON_MOVIE_CREDITS_ENDPOINT)
        self.api_key                                = configurations.configurations.get(KEYS.MOVIE_DB).get(KEYS.API_KEY)

    @timer
    @logger
    def get_person_details(self, name):
        """

        :param name:
        :return:
        """
        payload = {
            KEYS.API_KEY: self.api_key,
            STRINGS.QUERY: name
        }
        endpoint = self.get_search_person_endpoint

        return self._call_api(endpoint, payload)

    @timer
    @logger
    def get_person_movie_credits(self, person_id):
        """

        :param person_id:
        :return:
        """
        payload = {
            KEYS.API_KEY: self.api_key
        }
        endpoint = create_endpoint(self.get_person_movie_credits_base_endpoint, person_id=person_id)

        return self._call_api(endpoint, payload)

    @staticmethod
    def _call_api(endpoint, payload):
        """
        This functions call the given endpoint with the provided payload
        :param endpoint:
        :param payload:
        :return:
        """
        try:
            result = requests.get(endpoint, params=payload)
        except RequestException as e:
            print(e)
            return None
        except Exception as e:
            print(e)
            return None
        else:
            return result
