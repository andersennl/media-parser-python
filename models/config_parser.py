import os
import yaml

class ConfigParser:
	def __init__(self):
		dir = os.path.dirname(__file__)
		config_file = os.path.join(dir, '../config.yml')
		with open(config_file, 'r') as ymlfile:
			self.config = yaml.load(ymlfile)

	def series_path(self):
		return self.config["series"]

	def movies_path(self):
		return self.config["movies"]
