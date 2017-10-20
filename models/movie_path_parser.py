import os
from movie import Movie

class MoviePathParser:
  def __init__(self, path):
    self.path = path
    self.movies = []
  
  def parse(self):
    for movie in os.listdir(self.path):
        if not (movie.startswith(".")):
          self.movies.append(Movie(movie))
    return sorted(self.movies, key=lambda x: x.getName())
