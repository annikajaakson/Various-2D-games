import pygame
import sys
from math import ceil, floor
from random import randint, sample

# Muutujad ekraani mõõtmete jaoks + ruudustiku laius
grid = 20
screen_x = 41
screen_y = 33

enemies = []

win = False
lose = False

# Initsialiseeri pygame ja tekita ekraan
pygame.init()
screen = pygame.display.set_mode([screen_x*grid, screen_y*grid])

# Muutujad kasutatavate piltide jaoks
player_pic = pygame.image.load('maze_player.png')
tile_pic = pygame.image.load('maze_tile.png')
enemy_pic = pygame.image.load('maze_enemy.png')
prize_pic = pygame.image.load('maze_prize.png')
win_pic = pygame.image.load('maze_win.png')
lose_pic = pygame.image.load('maze_lose.png')


class Player:
    # Klass mängija jaoks

    def __init__(self, size):
        # Mängija omadused

        self.size = size
        self.x = 0
        self.y = 0
        self.spawn = randint(0, 3) # Labürindi külg, millel mängija välja ilmub

        # Vali mängija ilmumiskoht suvaliselt vastavalt muutujale self.spawn
        if self.spawn == 0:
            self.x = randint(0, screen_x-1)
        elif self.spawn == 1:
            self.y = screen_y - 1
            self.x = randint(0, screen_x-1)
        elif self.spawn == 2:
            self.y = randint(0, screen_y-1)
        elif self.spawn == 3:
            self.x = screen_x - 1
            self.y = randint(0, screen_y-1)

        # Mängija kiirust kontrollivad muutujad
        self.speed = 0.5
        self.cooldown = 3

    def update(self, maps, enemies):
        # Uuendab mängija asukohta

        global win, lose

        if self.cooldown == 0:
            self.cooldown = 3
            keymap = pygame.key.get_pressed()

            # Liigutab mängijat, kui võimalik (kui mängija ei põrka kokku labürindiga)
            dy = keymap[pygame.K_s] - keymap[pygame.K_w]
            dx = keymap[pygame.K_d] - keymap[pygame.K_a]

            if 0 <= self.x + dx < screen_x and 0 <= self.y + dy < screen_y:
                if maps.map[int(self.y) + dy][int(self.x) + dx] == 0:
                    self.x += dx
                    self.y += dy

            # Kokkupõrkamine vaenlastega
            for enemy in enemies:
                player_rect = pygame.Rect(self.x*grid, self.y*grid, self.size, self.size)
                enemy_rect = pygame.Rect(enemy.x*grid, enemy.y*grid, enemy.size, enemy.size)
                if player_rect.colliderect(enemy_rect):
                    lose = True
                    print("GAME OVER")

            # Mängija võidab mängu, kui satub labürindi keskele
            if self.x == screen_x/2-0.5 and self.y == screen_y/2-0.5:
                win = True
                print("YOU WIN")

        self.cooldown -= 1

    def draw(self, screen):
        # Joonistab mängija ekraanile

        screen.blit(player_pic, [self.x*grid, self.y*grid])


class Enemy:
    # Klass vaenlaste jaoks

    def __init__(self, x, y, e_type):
        # Vaenlase omadused

        self.x = x
        self.y = y
        self.e_type = e_type
        self.size = grid
        self.rect = None
        self.cooldown = 5
        self.dir = sample([-1, 1], 1)[0]
        self.speed = 0.25

    def update(self, e_map):
        # Uuendab vaenlaste asukohta

        # Genereerib vaenlaste suvalist liikumist
        if not self.cooldown:
            self.dir = sample([-1, 1], 1)[0]
            self.cooldown = 5

        # Liigutab vaenlast
        if 0 <= self.y + self.speed*self.dir <= screen_y - 1 and self.e_type:
            if self.dir == -1 and e_map.map[floor(self.y + self.speed*self.dir)][floor(self.x)] == 0:
                self.y += self.speed*self.dir
            elif self.dir == 1 and e_map.map[ceil(self.y + self.speed*self.dir)][ceil(self.x)] == 0:
                self.y += self.speed * self.dir

        elif 0 <= self.x + self.speed*self.dir <= screen_x - 1 and not self.e_type:
            if self.dir == -1 and e_map.map[floor(self.y)][floor(self.x + self.speed*self.dir)] == 0:
                self.x += self.speed*self.dir
            elif self.dir == 1 and e_map.map[ceil(self.y)][ceil(self.x + self.speed*self.dir)] == 0:
                self.x += self.speed*self.dir

        self.cooldown -= 1

    def draw(self, screen):
        # Joonistab vaenlase ekraanile

        screen.blit(enemy_pic, [self.x * grid, self.y * grid])


class Map:
    # Klass mänguväljaku ehk labürindi jaoks

    def __init__(self, bx, by):
        self.bx = bx
        self.by = by
        self.map = []

    def create(self, enemies):
        # Tekitab labürindi

        for y in range(self.by):
            self.map.append([])
            for x in range(self.bx):
                self.map[y].append(0)

        # Genereerib labürindi kontsentriliste ristkülikutena
        for i in range(1, int(self.by/2), 2):
            for j in range(i, self.bx-i, 1):
                self.map[i][j] = 1
                self.map[self.by-1-i][j] = 1

            # Loo üks läbipääs igasse ritta/veergu
            self.map[i][randint(i+1, self.bx-i-2)] = 0
            self.map[self.by - 1 - i][randint(i+1, self.bx-i-2)] = 0

            for k in range(i, self.by-1-i, 1):
                self.map[k][i] = 1
                self.map[k][self.bx-1-i] = 1

            # Loo üks läbipääs igasse ritta/veergu
            self.map[randint(i+1, self.by - i - 2)][i] = 0
            self.map[randint(i+1, self.by - i - 2)][self.bx - 1 - i] = 0

            # Loo vabadesse kohtadesse vaenlased (üks vaenlane rea/veeru kohta)
            if i != 1:
                enemies.append(Enemy(randint(i - 1, self.bx-i), i - 1, 0))
                enemies.append(Enemy(randint(i - 1, self.bx-i), self.by - i, 0))
                enemies.append(Enemy(i - 1, randint(i - 1, self.by-i), 1))
                enemies.append(Enemy(self.bx - i, randint(i - 1, self.by-i), 1))
            
    def draw(self, screen):
        # Joonista labürint ekraanile

        for y in range(self.by):
            for x in range(self.bx):
                if self.map[y][x] == 1:
                    screen.blit(tile_pic, [x * grid, y * grid])


# Loo mänguväljak, mängija ja genereeri vaenlased
maps = Map(screen_x, screen_y)
maps.create(enemies)
player = Player(grid)

while True:
    # Kontrollib mängu kinnipanekut
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Uuenda objektide asukohti ja joonista need ekraanile
    screen.fill([0, 0, 0])
    maps.draw(screen)

    if not win and not lose: # Kui mängu pole veel võidetud, uuendatakse mängija asukohta
        player.update(maps, enemies)

    screen.blit(prize_pic, [(screen_x/2-0.5)*grid, (screen_y/2-0.5)*grid])
    player.draw(screen)

    for enemy in enemies:
        enemy.update(maps)
        enemy.draw(screen)

    # Näita võidu- või kaotusteksti, kui vaja
    if win:
        screen.blit(win_pic, [0, 0])
    elif lose:
        screen.blit(lose_pic, [0, 0])

    # Näita muutusi ekraanil
    pygame.display.flip()
    pygame.time.wait(16)
