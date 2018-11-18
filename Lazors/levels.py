import pygame
import tilemap
import tilestack
import lazor
from constants import *


class Menu:
    def __init__(self):
        self.play = [MENU_START[0], MENU_START[1]]
        self.instr = [MENU_START[0], MENU_START[1] + MENU_BUTTON_H + MENU_BUTTON_GAP]
        self.exit = [MENU_START[0], MENU_START[1] + MENU_BUTTON_H * 2 + MENU_BUTTON_GAP * 2]
        self.playimg = pygame.image.load("playbutton.png")
        self.instrimg = pygame.image.load("instrbutton.png")
        self.exitimg = pygame.image.load("exitbutton.png")

    def update(self, mousedown):
        if mousedown:
            mouse_pos_pixel = pygame.mouse.get_pos()

            if self.play[0] < mouse_pos_pixel[0] < self.play[0] + MENU_BUTTON_W \
            and self.play[1] < mouse_pos_pixel[1] < self.play[1] + MENU_BUTTON_H:
                return LEVEL_RAND
            elif self.instr[0] < mouse_pos_pixel[0] < self.instr[0] + MENU_BUTTON_W \
            and self.instr[1] < mouse_pos_pixel[1] < self.instr[1] + MENU_BUTTON_H:
                return INSTR
            elif self.exit[0] < mouse_pos_pixel[0] < self.exit[0] + MENU_BUTTON_W \
            and self.exit[1] < mouse_pos_pixel[1] < self.exit[1] + MENU_BUTTON_H:
                return EXIT
            else:
                return MENU
        else:
            return MENU

    def draw(self, screen):
        screen.blit(self.playimg, self.play)
        screen.blit(self.instrimg, self.instr)
        screen.blit(self.exitimg, self.exit)


class Level:
    def __init__(self):
        self.tilemap = tilemap.Map()
        self.lazor = lazor.Lazor()
        self.tilestack = tilestack.Tilestack()

    def update(self, mousedown):
        self.tilemap.update(mousedown, self.lazor, self.tilestack)
        self.lazor.update(self.tilemap)

    def draw(self, screen):
        self.tilemap.draw(screen)
        self.lazor.draw(screen)
        self.tilestack.draw(screen)