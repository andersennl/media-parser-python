import os
import yaml
import datetime

#relative paths
dir = os.path.dirname(__file__)
config_file = os.path.join(dir, 'config.yml')
html_destination_path = os.path.join(dir, 'results.html')
updated_at = datetime.datetime.now().strftime("%H:%M:%S Uhr, %d.%m.%Y")

#load config
with open(config_file, 'r') as ymlfile:
    config = yaml.load(ymlfile)

series_path = config["series"]
movies_path = config["movies"]


class Movie:
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name.replace(".mkv", "")


class Series:
  def __init__(self, path, name):
    self.path = path
    self.name = name
    
  def getStaffeln(self):
    staffeln = []
    for staffel in os.listdir(self.path):
        if not (staffel.startswith(".")):
          new_staffel = Staffel(self.path+"/"+staffel, staffel)
          staffeln.append(new_staffel)
    return staffeln
    
  def getName(self):
    return self.name



class Staffel:
  def __init__(self, path, name):
    self.path = path
    self.name = name
  
  def getEpisodeCount(self):
    count = 0
    for episode in os.listdir(self.path):
      if not (episode.startswith(".")):
        count+=1
    return str(count)

  def getName(self):
    return self.name


class MoviePathParser:
  def __init__(self, path):
    self.path = path
    self.movies = []
  
  def parse(self):
    for movie in os.listdir(self.path):
        if not (movie.startswith(".")):
          self.movies.append(Movie(movie))
    return sorted(self.movies, key=lambda x: x.getName())



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
      serien.append(Series(series_path+"/"+serie, serie))

    return serien


with open(html_destination_path, 'w') as html:
  html_start = """<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Mediaserver running on NGINX</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" crossorigin="anonymous">
    </head>
    <body>
      <div class="container fluid">
        <div class="row">
          <div class="col-md-12">
            <h1>Mediaserver</h1>
            <p>Last updated at: """

  html_middle = """</p><p><a href="http://mediaserver.local:32400/web/index.html" target="_self">Plex Media Server</a></p>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12">
            <h2>Movies</h2>
            <p>"""
            
  html_after_movies = """</p>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12">
            <h2>Series</h2>
            <p>"""
            
  html_after_series = """</p>
          </div>
        </div>
      </div>
    </body>
  </html>"""



  html.write(html_start)
  html.write(updated_at)
  html.write(html_middle)



  # Movies
  movies = MoviePathParser(movies_path).parse()

  for movie in movies:
    html.write(movie.getName())
    html.write("<br>")

  html.write(html_after_movies)
  
  # Series
  serien = SeriesPathParser(series_path).parse()
      
  for serie in serien:
    html.write("<b>")
    html.write(serie.getName())
    html.write("</b>")
    html.write("<br>")

    for staffel in serie.getStaffeln():
      html.write(" " + staffel.getName() + ": " + staffel.getEpisodeCount() + " Episoden")
      html.write("<br>")
    html.write("<br>")
  
  html.write(html_after_series)

  print("Finished parsing")
