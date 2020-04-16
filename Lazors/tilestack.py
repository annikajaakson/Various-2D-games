import pygame
from constants import *
from helper_functions import *


class Tilestack:
    def __init__(self, nr_of_tiles=None):
        self.x = TILESTACK_LOCATION[0]
        self.y = TILESTACK_LOCATION[1]
        self.nr_of_tiles = nr_of_tiles

        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 40)
        self.text = self.font.render(' ∞', True, TILE_OCCUPIED_COLOR)
        if self.nr_of_tiles is not None:
            self.text = self.font.render(' ' + str(self.nr_of_tiles), True, TILE_OCCUPIED_COLOR)

    def update(self):
        if self.nr_of_tiles is None:
            self.text = self.font.render(' ∞', True, TILE_OCCUPIED_COLOR)
        else:
            self.text = self.font.render(' ' + str(self.nr_of_tiles), True, TILE_OCCUPIED_COLOR)

    def draw(self, screen, tilepics):
        stack = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)

        if self.nr_of_tiles is None or self.nr_of_tiles > 0:
            # stackcolor = TILE_OCCUPIED_COLOR
            screen.blit(tilepics[0], (stack.x, stack.y))
        else:
            # stackcolor = TILE_UNOCCUPIED_COLOR
            screen.blit(tilepics[1], (stack.x, stack.y))

        # pygame.draw.rect(screen, stackcolor, stack)
        screen.blit(self.text, (self.x + TILE_SIZE, self.y))