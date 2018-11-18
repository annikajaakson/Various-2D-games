import pygame
import sys
from constants import *
import tilemap
import tilestack
import lazor
import levels


class Game:
    def __init__(self):
        self.state = MENU
        self.menu = levels.Menu()
        self.level = None
        self.screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
        pygame.display.set_caption("Lazors")

        self.mousedown = False
        self.mousemoving = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mousedown = True
            elif event.type == pygame.MOUSEBUTTONUP and self.mousedown:
                self.mousedown = False
            elif event.type == pygame.MOUSEMOTION and self.mousedown:
                self.mousemoving = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.state = MENU
                self.level = None

    def draw_instr(self):
        # TODO: Actual instructions
        self.screen.fill(LAZOR_COLOR)

    def update(self):
        self.handle_events()

        if self.state == MENU:
            self.state = self.menu.update(self.mousedown)

            if self.state == LEVEL_RAND:
                self.level = levels.Level()
            elif self.state == EXIT:
                pygame.quit()
                sys.exit()
        elif self.state == INSTR:
            pass
        else:
            self.level.update(self.mousedown)

    def draw(self):
        self.screen.fill(BG_COLOR)

        if self.state == MENU:
            self.menu.draw(self.screen)
        elif self.state == INSTR:
            self.draw_instr()
        else:
            self.level.draw(self.screen)

    def run(self):
        while True:
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.wait(17)


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
