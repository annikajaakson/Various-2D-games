import pygame
import sys
import map
import player
from constants import *
from random import randint

basemap = [map.Basemap(0, 0, BASEWIDTH, SCREEN[1], GREEN), map.Basemap(SCREEN[0]-BASEWIDTH, 0, BASEWIDTH, SCREEN[1], GREEN)]
ornaments = [map.Ornaments(BASEWIDTH, 0, randint(1, 4), GREEN),
			 map.Ornaments(BASEWIDTH, 215, randint(1, 4), GREEN),
			 map.Ornaments(BASEWIDTH, 430, randint(1, 4), GREEN)]
player = player.Player(PLAYER_X, PLAYER_Y, YELLOW)

if __name__ == '__main__':
	pygame.init()
	
	screen = pygame.display.set_mode(SCREEN)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			for piece in ornaments:
				piece.event_handle(event)

			player.event_handle(event)
				
		screen.fill(BLUE)
		
		for piece in basemap:
			piece.draw(screen)
			
		for piece in ornaments:
			piece.update()
			piece.draw(screen)

		player.update()
		player.draw(screen)
		
		pygame.display.flip()
		pygame.time.wait(16)