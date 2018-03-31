import pygame
import sys
import maps
import player
from constants import *
from random import randint

# Create map and player
basemap = [maps.Basemap(0, 0, BASEWIDTH, SCREEN[1], GREEN), maps.Basemap(SCREEN[0]-BASEWIDTH, 0, BASEWIDTH, SCREEN[1], GREEN)]
ornaments = [maps.Ornaments(BASEWIDTH, 0, randint(1, 4), GREEN),
             maps.Ornaments(BASEWIDTH, 215, randint(1, 4), GREEN),
             maps.Ornaments(BASEWIDTH, 430, randint(1, 4), GREEN)]
player = player.Player(PLAYER_X, PLAYER_Y, YELLOW)

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(SCREEN)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for piece in ornaments:
                piece.event_handle(event)

            player.event_handle(event)

        # Update and draw everything on screen
        screen.fill(BLUE)

        for piece in basemap:
            piece.draw(screen)

        for piece in ornaments:
            piece.update()
            piece.draw(screen)

        player.update()
        player.draw(screen)

        # Show updates on screen
        pygame.display.flip()
        pygame.time.wait(16)
