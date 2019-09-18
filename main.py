#!/usr/bin/env python3

__author__ = "Shekhar Upadhaya <shekhar_8888@hotmail.com>"
__version__ = "0.1.0"

import argparse
from src.core.movie_app import MovieApp


def main(arguments):
    app = MovieApp(arguments.director_name)
    app.execute()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser(description="This script takes a movie director's name "
                                                 "and outputs the list of movies directed by him/her "
                                                 "(ordered by movie release date)")

    parser.add_argument("-n", "--director-name",
                        type=str,
                        required=True,
                        help="Name of the film director")

    args = parser.parse_args()

    main(args)
