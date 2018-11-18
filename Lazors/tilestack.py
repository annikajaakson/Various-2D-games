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
        self.text = self.font.render(' ∞', False, TILE_OCCUPIED_COLOR)
        if self.nr_of_tiles != None:
            self.text = self.font.render(str(self.nr_of_tiles), False, TILE_OCCUPIED_COLOR)

    def draw(self, screen):
        stack = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, TILE_OCCUPIED_COLOR, stack)
        screen.blit(self.text, (self.x + TILE_SIZE, self.y))