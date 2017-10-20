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

serien = []
movies = []

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
  
  def getEpisodenAnzahl(self):
    count = 0
    for episode in os.listdir(self.path):
      if not (episode.startswith(".")):
        count+=1
    return str(count)

  def getName(self):
    return self.name


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
  for movie in os.listdir(movies_path):
    if not (movie.startswith(".")):
      movies.append(movie)

  for movie in sorted(movies):
    html.write(movie.replace(".mkv", ""))
    html.write("<br>")

  html.write(html_after_movies)
  
  # Series
  serienTmp = []
  for serie in os.listdir(series_path):
    if not (serie.startswith(".")):
      serienTmp.append(serie)

  for serie in sorted(serienTmp):
    serien.append(Series(series_path+"/"+serie, serie))
      
  for serie in serien:
    html.write("<b>")
    html.write(serie.getName())
    html.write("</b>")
    html.write("<br>")

    for staffel in serie.getStaffeln():
      html.write(" " + staffel.getName() + ": " + staffel.getEpisodenAnzahl() + " Episoden")
      html.write("<br>")
    html.write("<br>")
  
  html.write(html_after_series)

  print("Finished parsing")
