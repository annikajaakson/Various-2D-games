from constants import *


def grid_to_pixel(grid):
    return [int(TILE_START[0] + grid[0] * TILE_SIZE), int(TILE_START[1] + grid[1] * TILE_SIZE)]


def pixel_to_grid(pixel):
    return [(pixel[0] - TILE_START[0]) / TILE_SIZE, (pixel[1] - TILE_START[1]) / TILE_SIZE]


def is_mouse_on_grid(mouse_pos):
    if mouse_pos[0] < TILE_START[0] or mouse_pos[0] > TILE_END[0] \
    or mouse_pos[1] < TILE_START[1] or mouse_pos[1] > TILE_END[1]:
        return False
    else:
        return True