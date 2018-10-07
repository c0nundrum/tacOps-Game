import pygame
import os
import MapParser.mapParser as mapParser
from collections import abc

pygame.init()

def is_wall(self, x, y):
	return self.get_bool(x, y, 'wall')

def render(self):
	wall = self.is_wall

def load_tile_table(name, width, height): #width and height of each tile
	
	#Loads the tileset
	tileSet = pygame.image.load(os.path.join('data', name)).convert()

	#Gets width and height
	img_width, img_heigth = tileSet.get_size()

	tile_table = []

	for tile_x in range(0, img_width//width):
		
		line = []
		tile_table.append(line)
		
		for tile_y in range(0, img_heigth//height):
			
			rect = (tile_x * width, tile_y * height, width, height)
			line.append(tileSet.subsurface(rect))

	return tile_table



def map_tiles(mapKeys): #returns a dict with the tile coords

	#Init the value for the tile Coordinates Dictionary
	tilesCoordinates = {}

	#save the key as the tile type and get the 'tile' set of coordinates from map
	# then add them to a dict
	for key, value in mapKeys.items():
		tile = key

		tilemapCoords = (mapKeys[key]['tile']).split(',')
		tilemapCoords = [int(i) for i in tilemapCoords]
		tilemapCoords = (tilemapCoords[0], tilemapCoords[1])

		tilesCoordinates[tile] = tilemapCoords
		
	return tilesCoordinates




if __name__ == '__main__':

	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	screen.fill((255, 255, 255))

	##load the tileset
	table = load_tile_table("Tileset01.png", 32, 32)
	

	##Load the mapParser
	levelLoader = mapParser.Level()
	tileMap = levelLoader.load_file()
	tileset = levelLoader.tileset
	tileKeys = levelLoader.key


	tileImageCoords = map_tiles(tileKeys)
	print(tileImageCoords)


	for y, row in enumerate(tileMap):
		for x, tile in enumerate(row):
			for k in tileImageCoords:
				try:
					#Take the tileImagesCoords for each of the key on the string version of the map and 
					# uses it as X and Y, since every tile is a key it works :)
					screen.blit(table[tileImageCoords[tile][1]][tileImageCoords[tile][0]], (x*32, y*32))

				except KeyError as e:
					#If there was a tile that does not have a coordinate value default to the wall
					screen.blit(table[6][0], (x*32, y*32))
				

	#Starts the main loop to display the screen
	mainLoop = True

	while mainLoop:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				mainLoop = False

		pygame.display.flip()

pygame.quit()