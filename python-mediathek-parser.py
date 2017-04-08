import os

serienPath = "/Users/nandersen/Desktop/python test/Serien"
filmePath = "/Users/nandersen/Desktop/python test/Filme"

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


# Filme
print("~Filme~")
for film in os.listdir(filmePath):
  if not (film.startswith(".")):
    print(film)
    
print(" ")
print(" ")

# Serien
print("~Serien~")
for serie in os.listdir(serienPath):
  if not (serie.startswith(".")):
    serien.append(Serie(serienPath+"/"+serie, serie))
    
for serie in serien:
  print(serie.getName())
  for staffel in serie.getStaffeln():
    print(" " + staffel.getName() + ": " + staffel.getEpisodenAnzahl() + " Episoden")