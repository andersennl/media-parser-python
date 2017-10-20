import os
from series import Series

class SeriesPathParser:
  def __init__(self, path):
    self.path = path

  def parse(self):
    series_tmp = []
    for serie in os.listdir(self.path):
      if not (serie.startswith(".")):
        series_tmp.append(serie)

    serien = []
    for serie in sorted(series_tmp):
      serien.append(Series(self.path+"/"+serie, serie))

    return serien
