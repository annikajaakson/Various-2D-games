import pygame
from settings import *


class Player:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.real_x = (SCREEN_W - PLAYER_SIZE) / 2
        self.real_y = (SCREEN_H - PLAYER_SIZE) / 2
        self.ver_speed = 0
        self.hor_speed = 0
        self.start = False
        self.coins = 0

        # Dying controls
        self.dead = False
        self.falling = False
        self.dead_y = self.real_y

    def handle_events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and keys[pygame.K_SPACE]:
            self.ver_speed = -8
            self.start = True
        elif keys[pygame.K_UP]:
            self.ver_speed = -1.5
            self.start = True

        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.hor_speed = 5
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.hor_speed = -5
        else:
            self.hor_speed = 0

    def collide(self, tilemap):
        dead = False

        if tilemap.grid[int(self.y / BLOCK_SIZE)][int(self.x / BLOCK_SIZE)] == 1 \
        or tilemap.grid[int((self.y + PLAYER_SIZE) / BLOCK_SIZE)][int(self.x / BLOCK_SIZE)] == 1 \
        or tilemap.grid[int(self.y / BLOCK_SIZE)][int((self.x + PLAYER_SIZE) / BLOCK_SIZE)] == 1 \
        or tilemap.grid[int((self.y + PLAYER_SIZE) / BLOCK_SIZE)][int((self.x + PLAYER_SIZE) / BLOCK_SIZE)] == 1:
            dead = True

        for tile in [[int((self.y + 20) / BLOCK_SIZE), int((self.x + 20) / BLOCK_SIZE)],
                     [int((self.y + PLAYER_SIZE - 2) / BLOCK_SIZE), int((self.x + 20) / BLOCK_SIZE)],
                     [int((self.y + 20) / BLOCK_SIZE), int((self.x + PLAYER_SIZE - 2) / BLOCK_SIZE)],
                     [int((self.y + PLAYER_SIZE - 2) / BLOCK_SIZE), int((self.x + PLAYER_SIZE - 2) / BLOCK_SIZE)]]:
            if tilemap.grid[tile[0]][tile[1]] == 2:
                self.coins += 1
                tilemap.grid[tile[0]][tile[1]] = 0

        return dead

    def update(self, tilemap):
        if not self.dead:
            self.handle_events()

            if self.start:
                self.y += self.ver_speed
                self.ver_speed += 0.5

                self.x += self.hor_speed

                self.dead = self.collide(tilemap)
        elif self.dead:
            if not self.falling:
                self.ver_speed = -20
                self.falling = True

            self.dead_y += self.ver_speed
            self.ver_speed += 1

    def draw(self, screen):
        if not self.dead:
            pygame.draw.rect(screen, PURPLE, [self.real_x, self.real_y, PLAYER_SIZE, PLAYER_SIZE])
        else:
            pygame.draw.rect(screen, PURPLE, [self.real_x, self.dead_y, PLAYER_SIZE, PLAYER_SIZE])
