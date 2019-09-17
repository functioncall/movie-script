import json
import time
import logging
from functools import wraps


def create_endpoint(base_endpoint, **kwargs):
    """
    This function takes base endpoint and replaces {key} with the passed {value} in it.
    So an endpoint like this: "https://api.themoviedb.org/3/person/{person_id}/movie_credits"
    becomes this: "https://api.themoviedb.org/3/person/123/movie_credits"

    :param base_endpoint:
    :param kwargs: Here kwargs key is same as the placeholder value in the base_endpoint to be replaced
                   and the kwargs value is the new value
    :return:
    """
    placeholder_key     = [key for key in kwargs.keys()][0]
    new_value           = kwargs[placeholder_key]
    placeholder_key     = '{' + placeholder_key + '}'

    endpoint = base_endpoint.replace(placeholder_key, new_value)

    return endpoint


def json_parser(obj):
    return json.loads(obj)


def is_empty(obj):
    if obj is None or obj == "" or obj == []:
        return True
    else:
        return False


def peek(iterable):
    """
    This function check whether a given generator is empty or not
    :param iterable:
    :return:
    """
    try:
        next(iterable)
    except StopIteration:
        return None
    return iterable


def timer(original_function):

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        tic = time.time()
        result = original_function(*args, **kwargs)
        toc = time.time()

        logging.info("{}() ran in {:.3f} sec".format(original_function.__name__, toc - tic))
        return result

    return wrapper
