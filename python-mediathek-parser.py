import os
import yaml

#config path
dir = os.path.dirname(__file__)
config_file = os.path.join(dir, 'config.yml')

#load config
with open(config_file, 'r') as ymlfile:
    config = yaml.load(ymlfile)

serienPath = config["serien"]
filmePath = config["filme"]

serien = []
filme = []

class Serie:
  def __init__(self, path, name):
    self.path = path
    self.name = name
    
  def getStaffeln(self):
    staffeln = []
    for staffel in os.listdir(self.path):
        if not (staffel.startswith(".")):
          staffeln.append(Staffel(self.path+"/"+staffel, staffel))
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
    return "{anzahl}".format(anzahl = count)

  def getName(self):
    return self.name


with open("results.html", 'w') as html:
  boilerplate = """<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Mediaserver running on NGINX</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    </head>
    <body>
      <div class="container fluid">
        <div class="row">
          <div class="col-md-12">
            <h1>Mediaserver</h1>
            <p><a href="http://mediaserver.local:32400/web/index.html" target="_self">Plex Media Server</a></p>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12">
            <h2>Filme</h2>
            <p>"""
            
  afterMovies = """</p>
          </div>
        </div>

        <div class="row">
          <div class="col-md-12">
            <h2>Serien</h2>
            <p>"""
            
  afterSerien = """</p>
          </div>
        </div>
      </div>
    </body>
  </html>"""

  html.write(boilerplate)
  







  # Filme
  for film in os.listdir(filmePath):
    if not (film.startswith(".")):
      filme.append(film)

  for film in sorted(filme):
    html.write(film)
    html.write("<br>")

  html.write(afterMovies)
  
  # Serien
  serienTmp = []
  for serie in os.listdir(serienPath):
    if not (serie.startswith(".")):
      serienTmp.append(serie)

  for serie in sorted(serienTmp):
    serien.append(Serie(serienPath+"/"+serie, serie))
      
  for serie in serien:
    html.write("<b>")
    html.write(serie.getName())
    html.write("</b>")
    html.write("<br>")

    for staffel in serie.getStaffeln():
      html.write(" " + staffel.getName() + ": " + staffel.getEpisodenAnzahl() + " Episoden")
      html.write("<br>")
    html.write("<br>")
  
  html.write(afterSerien)
