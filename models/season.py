import os

class Season:
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
