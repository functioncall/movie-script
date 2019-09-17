"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import unittest

from unittest.mock import patch
from src.modules.dao import Dao
from src.common.configurations import configurations
from src.common import KEYS, STRINGS


class TestDao(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dao = Dao()
        cls.api_key = configurations.get(KEYS.MOVIE_DB).get(KEYS.API_KEY)

    @classmethod
    def tearDownClass(cls):
        cls.dao = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_person_details(self):
        with patch('src.modules.dao.requests.get') as mocked_get:
            self.dao.get_person_details("Quentin Tarantino")
            mocked_get.assert_called_with(
                'https://api.themoviedb.org/3/search/person',
                params={
                    KEYS.API_KEY: self.api_key,
                    STRINGS.QUERY: 'Quentin Tarantino'
                }
            )

    def test_get_person_movie_credits(self):
        with patch('src.modules.dao.requests.get') as mocked_get:
            self.dao.get_person_movie_credits('138')
            mocked_get.assert_called_with(
                'https://api.themoviedb.org/3/person/138/movie_credits',
                params={
                    KEYS.API_KEY: self.api_key,
                }
            )


if __name__ == '__main__':
    unittest.main()
