import os
import logging
from functools import wraps


def logger(original_function):
    logging.basicConfig(
        filename=os.path.join(os.getcwd(), "log/application.log"),
        level=logging.INFO,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M'
    )

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        logging.info("Ran {}() with args: {} ".format(original_function.__name__, args[1:]))
        return original_function(*args, **kwargs)

    return wrapper
