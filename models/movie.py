class Movie:
  def __init__(self, name):
    self.name = name

  def getName(self):
    return self.name.replace(".mkv", "")
