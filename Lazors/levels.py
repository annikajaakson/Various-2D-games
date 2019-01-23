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
        self.playimg = pygame.image.load("mangbutton.png")
        self.instrimg = pygame.image.load("juhendbutton.png")
        self.exitimg = pygame.image.load("valjubutton.png")

        self.showlevels = False
        self.cooldown = 10

        self.level_images = [pygame.image.load("lvl1.png"),
                             pygame.image.load("lvl2.png"),
                             pygame.image.load("lvl3.png"),
                             pygame.image.load("lvl4.png"),
                             pygame.image.load("lvl5.png"),
                             pygame.image.load("lvlRAND.png")]

        self.level_image_locs = []
        for i, lvl_img in enumerate(self.level_images):
                self.level_image_locs.append([LEVEL_START[0] + (i % 3) * (LEVEL_BUTTON_SIZE + LEVEL_BUTTON_GAP),
                                              LEVEL_START[1] + int(i / 3) * (LEVEL_BUTTON_SIZE + LEVEL_BUTTON_GAP)])

    def update(self, mousedown):
        if mousedown and not self.showlevels:
            mouse_pos_pixel = pygame.mouse.get_pos()

            if self.play[0] < mouse_pos_pixel[0] < self.play[0] + MENU_BUTTON_W \
            and self.play[1] < mouse_pos_pixel[1] < self.play[1] + MENU_BUTTON_H:
                self.showlevels = True
                self.cooldown = 10
                return MENU
            elif self.instr[0] < mouse_pos_pixel[0] < self.instr[0] + MENU_BUTTON_W \
            and self.instr[1] < mouse_pos_pixel[1] < self.instr[1] + MENU_BUTTON_H:
                return INSTR
            elif self.exit[0] < mouse_pos_pixel[0] < self.exit[0] + MENU_BUTTON_W \
            and self.exit[1] < mouse_pos_pixel[1] < self.exit[1] + MENU_BUTTON_H:
                return EXIT
            else:
                return MENU
        elif mousedown and self.showlevels and not self.cooldown:
            mouse_pos_pixel = pygame.mouse.get_pos()

            for l, img_loc in enumerate(self.level_image_locs):
                if img_loc[0] < mouse_pos_pixel[0] < img_loc[0] + LEVEL_BUTTON_SIZE \
                and img_loc[1] < mouse_pos_pixel[1] < img_loc[1] + LEVEL_BUTTON_SIZE:
                    return l + 1 # Return enumeration value of given level

            return MENU
        else:
            if self.showlevels and self.cooldown:
                self.cooldown -= 1
            return MENU

    def draw(self, screen):
        if self.showlevels:
            for i, lvl_img in enumerate(self.level_images):
                screen.blit(lvl_img, self.level_image_locs[i])
        else:
            screen.blit(self.playimg, self.play)
            screen.blit(self.instrimg, self.instr)
            screen.blit(self.exitimg, self.exit)


class Level:
    def __init__(self, index):
        if index == LEVEL_1:
            self.tilemap = tilemap.Map(LVL1["CHECKPOINTS"])
            self.lazor = lazor.Lazor(LVL1["LAZOR_SPAWN"], LVL1["LAZOR_DIR"])
            self.tilestack = tilestack.Tilestack(LVL1["TILES"])
        elif index == LEVEL_2:
            self.tilemap = tilemap.Map(LVL2["CHECKPOINTS"])
            self.lazor = lazor.Lazor(LVL2["LAZOR_SPAWN"], LVL2["LAZOR_DIR"])
            self.tilestack = tilestack.Tilestack(LVL2["TILES"])
        elif index == LEVEL_3:
            self.tilemap = tilemap.Map(LVL3["CHECKPOINTS"])
            self.lazor = lazor.Lazor(LVL3["LAZOR_SPAWN"], LVL3["LAZOR_DIR"])
            self.tilestack = tilestack.Tilestack(LVL3["TILES"])
        elif index == LEVEL_4:
            self.tilemap = tilemap.Map(LVL4["CHECKPOINTS"])
            self.lazor = lazor.Lazor(LVL4["LAZOR_SPAWN"], LVL4["LAZOR_DIR"])
            self.tilestack = tilestack.Tilestack(LVL4["TILES"])
        elif index == LEVEL_5:
            self.tilemap = tilemap.Map(LVL5["CHECKPOINTS"])
            self.lazor = lazor.Lazor(LVL5["LAZOR_SPAWN"], LVL5["LAZOR_DIR"])
            self.tilestack = tilestack.Tilestack(LVL5["TILES"])
        elif index == LEVEL_RAND:
            self.tilemap = tilemap.Map()
            self.lazor = lazor.Lazor(LVLRAND["LAZOR_SPAWN"], LVLRAND["LAZOR_DIR"])
            self.tilestack = tilestack.Tilestack()

        self.empty_tile = pygame.image.load("emptytile.png")
        self.occupied_tile = pygame.image.load("tile.png")

    def update(self, mousedown):
        self.tilemap.update(mousedown, self.lazor, self.tilestack)
        self.lazor.update(self.tilemap)
        self.tilestack.update()

    def draw(self, screen):
        self.tilestack.draw(screen, (self.occupied_tile, self.empty_tile))
        self.tilemap.draw_grid(screen)
        self.lazor.draw(screen)
        self.tilemap.draw_tiles(screen)
