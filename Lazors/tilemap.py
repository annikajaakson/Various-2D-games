import pygame
from random import randint
from constants import *
from helper_functions import *


class Checkpoint:
    def __init__(self, x, y):
        self.location = grid_to_pixel([x, y])
        self.passed = False
        self.color = CHECKPOINT_COLOR

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self.color,
                           self.location,
                           LAZORHEAD_RADIUS)


class FreeTile:
    def __init__(self, mouse_pos_pixel, fromstack):
        self.fromstack = fromstack  # If tile was taken from stack, boolean
        self.mouse_pos_pixel = mouse_pos_pixel
        self.mouse_pos_grid = pixel_to_grid(self.mouse_pos_pixel)
        self.tile_orig_location = [int(self.mouse_pos_grid[0]), int(self.mouse_pos_grid[1])]

        if self.fromstack:
            self.tile_pos_pixel = TILESTACK_LOCATION
        else:
            self.tile_pos_pixel = grid_to_pixel(self.tile_orig_location)

        self.drag_offset = (self.mouse_pos_pixel[0] - self.tile_pos_pixel[0],
                            self.mouse_pos_pixel[1] - self.tile_pos_pixel[1])
        self.tile = pygame.Rect(self.tile_pos_pixel[0], self.tile_pos_pixel[1], TILE_SIZE, TILE_SIZE)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.tile.x = mouse_pos[0] - self.drag_offset[0]
        self.tile.y = mouse_pos[1] - self.drag_offset[1]

    def draw(self, screen):
        pygame.draw.rect(screen, TILE_OCCUPIED_COLOR, self.tile)


class Map:
    def __init__(self, checkcoords=None):
        self.grid = [[0 for i in range(GRID_W)] for j in range(GRID_H)]
        self.freetile = None
        self.checkcoords = checkcoords
        self.checkpoints = []

        if checkcoords:
            for cp in checkcoords:
                self.checkpoints.append(Checkpoint(cp[0], cp[1]))
        else:
            for nr_of_checkpoints in range(randint(1, 5)):
                checkpoint_x = randint(0, 20) / 2
                if (checkpoint_x / 0.5) % 2:
                    checkpoint_y = randint(0, 10)
                else:
                    checkpoint_y = randint(0, 9) + 0.5
                self.checkpoints.append(Checkpoint(checkpoint_x, checkpoint_y))

    def update(self, mousedown, lazor, tilestack):
        # If mouse is pressed and no free tile is being held
        if mousedown and not self.freetile:
            mouse_pos_pixel = pygame.mouse.get_pos()
            mouse_pos_grid = pixel_to_grid(mouse_pos_pixel)

            if is_mouse_on_grid(mouse_pos_pixel) \
            and self.grid[int(mouse_pos_grid[1])][int(mouse_pos_grid[0])] != 0:
                self.grid[int(mouse_pos_grid[1])][int(mouse_pos_grid[0])] = 0
                self.freetile = FreeTile(mouse_pos_pixel, fromstack=False)
            elif tilestack.nr_of_tiles > 0 \
            and tilestack.x < mouse_pos_pixel[0] < tilestack.x + TILE_SIZE \
            and tilestack.y < mouse_pos_pixel[1] < tilestack.y + TILE_SIZE:
                self.freetile = FreeTile(mouse_pos_pixel, fromstack=True)
                tilestack.nr_of_tiles -= 1

        # If mouse is released and the free tile is being held
        elif not mousedown:
            if self.freetile:
                tile_pos = pixel_to_grid([self.freetile.tile.x + TILE_SIZE / 2, self.freetile.tile.y + TILE_SIZE / 2])

                if self.freetile.fromstack \
                and (tile_pos[0] < 0 or tile_pos[0] > GRID_W or tile_pos[1] < 0 or tile_pos[1] > GRID_H):
                    tilestack.nr_of_tiles += 1
                else:
                    if (tile_pos[0] < 0 or tile_pos[0] > GRID_W or tile_pos[1] < 0 or tile_pos[1] > GRID_H) \
                    or self.grid[int(tile_pos[1])][int(tile_pos[0])] != 0:
                        self.grid[self.freetile.tile_orig_location[1]][self.freetile.tile_orig_location[0]] = 1
                    elif self.grid[int(tile_pos[1])][int(tile_pos[0])] == 0:
                        self.grid[int(tile_pos[1])][int(tile_pos[0])] = 1

                self.freetile = None

                for checkpoint in self.checkpoints:
                    checkpoint_loc = pixel_to_grid(checkpoint.location)
                    checkpoint.__init__(checkpoint_loc[0], checkpoint_loc[1])
                lazor.created = False
                lazor.__init__(lazor.spawn_location, lazor.orig_direction)

        # Update free tile if it exists
        if self.freetile:
            for checkpoint in self.checkpoints:
                checkpoint_loc = pixel_to_grid(checkpoint.location)
                checkpoint.__init__(checkpoint_loc[0], checkpoint_loc[1])
            lazor.created = False
            lazor.__init__(lazor.spawn_location, lazor.orig_direction)
            self.freetile.update()

    def draw_grid(self, screen):
        # Draw unoccupied tiles on screen
        for tile_y in range(GRID_H):
            for tile_x in range(GRID_W):
                # Locate current rectangle according to TILE_START and x & y coordinates
                current_rect = [TILE_START[0] + TILE_SIZE * tile_x + TILE_GAP / 2,
                                TILE_START[1] + TILE_SIZE * tile_y + TILE_GAP / 2,
                                TILE_SIZE - TILE_GAP,
                                TILE_SIZE - TILE_GAP]

                if self.grid[tile_y][tile_x] == 0:
                    pygame.draw.rect(screen, TILE_UNOCCUPIED_COLOR, current_rect)

        # Draw checkpoints on screen
        for checkpoint in self.checkpoints:
            checkpoint.draw(screen)

    def draw_tiles(self, screen):
        # Draw occupied tiles on screen
        for tile_y in range(GRID_H):
            for tile_x in range(GRID_W):
                # Locate current rectangle according to TILE_START and x & y coordinates
                current_rect = [TILE_START[0] + TILE_SIZE * tile_x + TILE_GAP / 2,
                                TILE_START[1] + TILE_SIZE * tile_y + TILE_GAP / 2,
                                TILE_SIZE - TILE_GAP,
                                TILE_SIZE - TILE_GAP]

                if self.grid[tile_y][tile_x] == 1:
                    pygame.draw.rect(screen, TILE_OCCUPIED_COLOR, current_rect)

        # Draw the tile being held if it exists
        if self.freetile:
            self.freetile.draw(screen)
