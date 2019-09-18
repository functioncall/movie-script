
import logging

from src.core.i_app import App
from src.model.director import Director


class MovieApp(App):

    def __init__(self, director_name):
        self.director_name = director_name

    def execute(self):
        logging.info(f"######### Script initiated for person <{self.director_name}> ##########")

        director = Director(self.director_name)

        if director.movies is not None:
            director.list_movies()
