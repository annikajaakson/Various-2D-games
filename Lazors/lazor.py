import pygame
from math import sin, cos, tan, pi, ceil, floor
from random import randint
from constants import *
from helper_functions import *


class Ray:
    def __init__(self, direction, ray_type, start_x, start_y, end_x=None, end_y=None):
        self.direction = direction # NE, SE, SW, NW
        self.ray_type = ray_type
        # Convert start coordinates from grid to pixel coordinates
        self.start = [int(TILE_START[0] + start_x * TILE_SIZE), int(TILE_START[1] + start_y * TILE_SIZE)]
        self.end = [end_x, end_y]

    def update(self):
        pass

    def draw(self, screen):
        if self.ray_type == RAY_ENDLESS:
            # Find ray endpoint location if it doesn't reflect on tiles
            if self.direction == SE:
                self.end[0] = SCREEN_W
                self.end[1] = int(self.start[1] + round(tan(pi/4)) * (SCREEN_W - self.start[0]))
            elif self.direction == SW:
                self.end[0] = 0
                self.end[1] = int(self.start[1] + round(tan(pi/4)) * self.start[0])
            elif self.direction == NE:
                self.end[0] = int(self.start[0] + round(tan(pi/4)) * self.start[1])
                self.end[1] = 0
            elif self.direction == NW:
                self.end[0] = int(self.start[0] - round(tan(pi/4)) * self.start[1])
                self.end[1] = 0

        pygame.draw.line(screen, LAZOR_COLOR, self.start, self.end, LAZOR_THICKNESS)


class Lazor:
    def __init__(self, spawn_loc, orig_dir):
        self.spawn_location = spawn_loc
        self.orig_direction = orig_dir
        self.ray_array = [Ray(self.orig_direction, RAY_ENDLESS, self.spawn_location[0], self.spawn_location[1])]
        self.created = False

    def create(self, tilemap):
        out_of_bounds = False
        add_new_ray = False
        ray_index = 0
        current_loc = pixel_to_grid(self.ray_array[ray_index].start) # In grid coordinates

        while not out_of_bounds:
            if (current_loc[0] / 0.5) % 2: # If x-coordinate of current location is on half a tile
                # If direction is NE or NW
                if (self.ray_array[ray_index].direction == NE or self.ray_array[ray_index].direction == NW) \
                and tilemap.grid[floor(current_loc[1]) - 1][floor(current_loc[0])]:
                    add_new_ray = True
                # If direction is SE or SW
                elif (self.ray_array[ray_index].direction == SE or self.ray_array[ray_index].direction == SW) \
                and tilemap.grid[floor(current_loc[1])][floor(current_loc[0])]:
                    add_new_ray = True
            else:
                # If direction is NE or SE
                if (self.ray_array[ray_index].direction == NE or self.ray_array[ray_index].direction == SE) \
                and tilemap.grid[floor(current_loc[1])][floor(current_loc[0])]:
                    add_new_ray = True
                # If direction is NW or SW
                elif (self.ray_array[ray_index].direction == NW or self.ray_array[ray_index].direction == SW) \
                and tilemap.grid[floor(current_loc[1])][floor(current_loc[0]) - 1]:
                    add_new_ray = True

            if add_new_ray:
                self.ray_array[ray_index].end = grid_to_pixel(current_loc)
                self.ray_array[ray_index].ray_type = RAY_ENDING

                if self.ray_array[ray_index].direction == SE:
                    if (current_loc[0] / 0.5) % 2:
                        self.ray_array.append(Ray(NE, RAY_ENDLESS, current_loc[0], current_loc[1]))
                    else:
                        self.ray_array.append(Ray(SW, RAY_ENDLESS, current_loc[0], current_loc[1]))
                elif self.ray_array[ray_index].direction == SW:
                    if (current_loc[0] / 0.5) % 2:
                        self.ray_array.append(Ray(NW, RAY_ENDLESS, current_loc[0], current_loc[1]))
                    else:
                        self.ray_array.append(Ray(SE, RAY_ENDLESS, current_loc[0], current_loc[1]))
                elif self.ray_array[ray_index].direction == NW:
                    if (current_loc[0] / 0.5) % 2:
                        self.ray_array.append(Ray(SW, RAY_ENDLESS, current_loc[0], current_loc[1]))
                    else:
                        self.ray_array.append(Ray(NE, RAY_ENDLESS, current_loc[0], current_loc[1]))
                elif self.ray_array[ray_index].direction == NE:
                    if (current_loc[0] / 0.5) % 2:
                        self.ray_array.append(Ray(SE, RAY_ENDLESS, current_loc[0], current_loc[1]))
                    else:
                        self.ray_array.append(Ray(NW, RAY_ENDLESS, current_loc[0], current_loc[1]))

                ray_index += 1
                add_new_ray = False

            if self.ray_array[ray_index].direction == SE:
                current_loc[0] += 0.5
                current_loc[1] += 0.5
            elif self.ray_array[ray_index].direction == SW:
                current_loc[0] -= 0.5
                current_loc[1] += 0.5
            elif self.ray_array[ray_index].direction == NW:
                current_loc[0] -= 0.5
                current_loc[1] -= 0.5
            elif self.ray_array[ray_index].direction == NE:
                current_loc[0] += 0.5
                current_loc[1] -= 0.5

            for checkpoint in tilemap.checkpoints:
                if checkpoint.location == grid_to_pixel(current_loc):
                    checkpoint.passed = True
                    checkpoint.color = LAZOR_COLOR

            if current_loc[0] > GRID_W - 0.5 or current_loc[0] <= 0 \
            or current_loc[1] > GRID_H - 0.5 or current_loc[1] <= 0:
                out_of_bounds = True

            if current_loc[0] == float(self.spawn_location[0]) \
            and current_loc[1] == float(self.spawn_location[1]) \
            and self.ray_array[ray_index].direction == self.orig_direction:
                self.ray_array[ray_index].end = grid_to_pixel(self.spawn_location)
                self.ray_array[ray_index].ray_type = RAY_ENDING
                out_of_bounds = True

    def update(self, tilemap):
        if not self.created:
            self.create(tilemap)
            self.created = True

    def draw(self, screen):
        pygame.draw.circle(screen,
                           LAZOR_COLOR,
                           [int(TILE_START[0] + self.spawn_location[0] * TILE_SIZE),
                            int(TILE_START[1] + self.spawn_location[1] * TILE_SIZE)],
                           LAZORHEAD_RADIUS)

        for ray in self.ray_array:
            ray.update()
            ray.draw(screen)
