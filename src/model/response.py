from src.modules.utilities import json_parser
from src.modules.utilities import is_empty


class Response:
    """
    Abstract class to handle api response
    """
    def get_instance(self):
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
        self.data  = data

    def get_instance(self):
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


class GetPersonMovieCreditsResponse(Response):
    """
    This class handles get person movie credits response data
    """
    def __init__(self, data):
        self.data = data

    def get_instance(self):
        if not is_empty(self.data):
            result = json_parser(self.data.content)

            if not result:
                return None
            else:
                return result
        else:
            return None
