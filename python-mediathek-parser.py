import os
import time
import datetime

from models.series import Series
from models.config_parser import ConfigParser
from models.movie_path_parser import MoviePathParser
from models.series_path_parser import SeriesPathParser

time_start = time.time()
updated_at = datetime.datetime.now().strftime("%H:%M:%S Uhr, %d.%m.%Y")

dir = os.path.dirname(__file__)
html_destination_path = os.path.join(dir, 'results.html')

with open(html_destination_path, 'w') as html:
  html_start = """
    <!DOCTYPE html>
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

  html_middle = """
              </p><p><a href="http://mediaserver.local:32400/web/index.html" target="_self">Plex Media Server</a></p>
            </div>
          </div>

          <div class="row">
            <div class="col-md-12">
              <h2>Filme</h2>
              <p>"""
            
  html_after_movies = """
              </p>
            </div>
          </div>

          <div class="row">
            <div class="col-md-12">
              <h2>Serien</h2>
              <p>"""
            
  html_after_series = """
              </p>
            </div>
          </div>
        </div>
      </body>
    </html>"""



  html.write(html_start)
  html.write(updated_at)
  html.write(html_middle)



  # Movies
  parser = ConfigParser()
  movies = MoviePathParser(parser.movies_path()).parse()

  for movie in movies:
    html.write(movie.getName())
    html.write("<br>")

  html.write(html_after_movies)
  
  # Series
  serien = SeriesPathParser(parser.series_path()).parse()
      
  for serie in serien:
    html.write("<b>")
    html.write(serie.getName())
    html.write("</b>")
    html.write("<br>")

    for staffel in serie.getStaffeln():
      html.write(" " + staffel.getName() + ": " + staffel.getEpisodeCount() + " Episoden")
      html.write("<br>")
    html.write("<br>")
  
  html.write("<br>")
  html.write("<b>")

  parsing_time = time.time() - time_start
  html.write("Finished parsing in %.3f seconds" % (parsing_time))

  html.write("</b>")

  html.write(html_after_series)

  print("Finished parsing in %.3f seconds" % (parsing_time))
