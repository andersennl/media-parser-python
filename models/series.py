import os
from season import Season

class Series:
  def __init__(self, path, name):
    self.path = path
    self.name = name

  def getName(self):
    return self.name
    
  def getStaffeln(self):
    staffeln = []
    for staffel in os.listdir(self.path):
        if not (staffel.startswith(".")):
          new_staffel = Season(self.path+"/"+staffel, staffel)
          staffeln.append(new_staffel)
    return sorted(staffeln, key=lambda x: x.getName())
