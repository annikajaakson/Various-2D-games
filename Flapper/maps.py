import pygame
from settings import *


class Map:
    def __init__(self):
        self.grid = []

        with open("map.txt", 'r') as mapsrc:
            for line in mapsrc.readlines():
                self.grid.append([int(i) for i in line.strip("\n").split(" ")])

    def draw(self, screen, player_loc, player_real_loc):
        for r, row in enumerate(self.grid):
            for c, column in enumerate(row):
                if self.grid[r][c] == 1:
                    pygame.draw.rect(screen, GREEN, [c * BLOCK_SIZE - player_loc[0] + player_real_loc[0],
                                                     r * BLOCK_SIZE - player_loc[1] + player_real_loc[1],
                                                     BLOCK_SIZE,
                                                     BLOCK_SIZE])
                elif self.grid[r][c] == 2:
                    pygame.draw.circle(screen,
                                       YELLOW,
                                       [int(c * BLOCK_SIZE - player_loc[0] + player_real_loc[0]),
                                        int(r * BLOCK_SIZE - player_loc[1] + player_real_loc[1])],
                                       int(BLOCK_SIZE / 2 - 5))
