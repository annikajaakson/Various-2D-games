import pygame
import sys
import maps
import player
from constants import *
from random import randint

# Create map and player
basemap = [maps.Basemap(0, 0, BASEWIDTH, SCREEN[1], GREEN), maps.Basemap(SCREEN[0]-BASEWIDTH, 0, BASEWIDTH, SCREEN[1], GREEN)]
ornaments = [maps.Ornaments(BASEWIDTH, 0, randint(1, 4), GREEN),
             maps.Ornaments(BASEWIDTH, 215, 1, GREEN),
             maps.Ornaments(BASEWIDTH, 430, randint(1, 4), GREEN)]
player = player.Player(PLAYER_X, PLAYER_Y, YELLOW)

lose_counter = 512
lose_screen = pygame.Surface((SCREEN[0], SCREEN[1]))

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(SCREEN)

    clock = pygame.time.Clock()

    bg = pygame.image.load("bg.png")
    lose = pygame.image.load("gameover.png")

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if player.lives > 0:
                for piece in ornaments:
                    piece.event_handle(event)

            player.event_handle(event)

        # Update and draw everything on screen
        screen.blit(bg, (0, 0))

        for piece in basemap:
            piece.draw(screen)

        for piece in ornaments:
            if player.lives <= 0:
                piece.speed = 0
            piece.update()
            piece.draw(screen)

        if lose_counter >= 256:
            player.update(ornaments)
            player.draw(screen)

        if player.lives <= 0 and lose_counter:
            if lose_counter > 256:
                lose_counter -= 64
                lose_screen.set_alpha(256 - lose_counter % 256)
            else:
                lose_counter -= 1
                lose_screen.set_alpha(lose_counter % 256)

        if player.lives <= 0:
            if lose_counter <= 256:
                # TODO: You lost screen
                screen.blit(lose, (SCREEN[0] / 2 - 100, SCREEN[1] / 2 - 100))
            lose_screen.fill(WHITE)
            screen.blit(lose_screen, (0, 0))

        # Show updates on screen
        pygame.display.flip()
        clock.tick(60)
