import pygame
import os

pygame.init()

def load_tile_table(name, width, height): #width and height of each tile
	
	#Loads the tileset
	tileSet = pygame.image.load(os.path.join('data', name)).convert()

	#Gets width and height
	img_width, img_heigth = tileSet.get_size()
	print(img_heigth)
	print(img_width)

	tile_table = []

	for tile_x in range(0, img_width//width):
		
		line = []
		tile_table.append(line)
		
		for tile_y in range(0, img_heigth//height):
			
			rect = (tile_x * width, tile_y * height, width, height)
			line.append(tileSet.subsurface(rect))

	return tile_table


if __name__ == '__main__':

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    screen.fill((255, 255, 255))
    table = load_tile_table("Tileset01.png", 32, 32)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*50, y*50))
    
    
    mainLoop = True

    while mainLoop:
    	for event in pygame.event.get():
	    	if event.type == pygame.QUIT:
	    		mainLoop = False

    	pygame.display.flip()

pygame.quit()