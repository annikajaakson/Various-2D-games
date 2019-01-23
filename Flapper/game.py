import sys
import pygame
import player
import maps
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        pygame.display.set_caption("Flapper")
        self.clock = pygame.time.Clock()

        self.score = 0
        self.scorefont = pygame.font.SysFont("Arial", 40)
        self.scoretext = self.scorefont.render("SKOOR: " + str(self.score), True, WHITE)

        self.hero = player.Player(19 * BLOCK_SIZE, 6 * BLOCK_SIZE)
        self.tilemap = maps.Map()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.handle_events()
        self.hero.update(self.tilemap)

        self.score = self.hero.coins
        self.scoretext = self.scorefont.render("SKOOR: " + str(self.score), True, WHITE)

    def draw(self):
        self.screen.fill(BLUE)
        self.tilemap.draw(self.screen, [self.hero.x, self.hero.y], [self.hero.real_x, self.hero.real_y])
        self.hero.draw(self.screen)
        self.screen.blit(self.scoretext, [20, 20])

    def run(self):
        while True:
            if self.hero.dead and self.hero.dead_y > 6 * SCREEN_H:
                self.__init__()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
