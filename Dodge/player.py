import pygame
from constants import *
from helper_functions import *


class Player():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.shape = pygame.Rect([self.x, self.y, PLAYER_SIZE, PLAYER_SIZE])
        self.speed = 0
        self.direction = 0
        self.lives = 1
        self.collided = False
        self.img = pygame.image.load("player.png")

    def draw(self, screen):
        self.shape = pygame.Rect([self.x, self.y, PLAYER_SIZE, PLAYER_SIZE])
        screen.blit(self.img, (self.x, self.y))

    def event_handle(self, event):
        # Change direction if A/LEFT or D/RIGHT is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if self.direction == 0:
                    self.direction = 1
                    self.speed = 5
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if self.direction == 0:
                    self.direction = 2
                    self.speed = 5

        # If A/LEFT or D/RIGHT is released, change direction back to 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.direction = 0
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.direction = 0

    # Check if player rectangle collides with obstacles
    def collide(self, targets):
        for target in targets:
            if target.index == 1 or target.index == 3:
                for t_shape in target.shapes:
                    if self.shape.colliderect(t_shape):
                        return True

            elif target.index == 2 or target.index == 4:
                for t_shape in target.shapes:
                    for point in t_shape:
                        if self.x < point[0] < self.x + PLAYER_SIZE \
                        and self.y < point[1] < self.y + PLAYER_SIZE:
                            return True

                for point in [[self.x, self.y], [self.x + PLAYER_SIZE, self.y],
                              [self.x, self.y + PLAYER_SIZE], [self.x + PLAYER_SIZE, self.y + PLAYER_SIZE]]:
                    for t_shape in target.shapes:
                        if point_inside_triangle(t_shape[0], t_shape[1], t_shape[2], point):
                            return True

    def update(self, targets):
        collision = self.collide(targets)
        if collision and not self.collided:
            self.lives -= 1
            self.collided = True
            if self.lives == 0:
                self.direction = 0
        elif not collision and self.collided:
            self.collided = False

        # Move according to direction
        if self.direction == 1:
            if (self.x - self.speed) >= BASEWIDTH:
                self.x -= self.speed
        elif self.direction == 2:
            if (self.x + self.speed) <= SCREEN[0]-BASEWIDTH-PLAYER_SIZE:
                self.x += self.speed
        elif self.direction == 0:
            if self.x < PLAYER_X:
                self.x += self.speed
            elif self.x > PLAYER_X:
                self.x -= self.speed