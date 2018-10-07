import configparser
import os

class Level(object):

	def __init__(self):
		self.tileset = None
		self.mapTiles = []
		self.key = {}

	def load_file(self, filename='level01.level'):

		parser = configparser.ConfigParser()
		parser.read(os.path.join('data', filename))
		self.tileset = parser.get('level', 'tileset')
		self.mapTiles = parser.get('level', 'map').split('\n')
		for section in parser.sections():
			if len(section) == 1:
				desc = dict(parser.items(section))
				self.key[section] = desc


		return self.mapTiles



if __name__ == '__main__':
	
	levelLoader = Level()
	levelLoader.load_file()

	for tile in levelLoader.mapTiles:
		print(tile)