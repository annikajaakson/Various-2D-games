MENU = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVEL_4 = 4
LEVEL_5 = 5
LEVEL_RAND = 6
LEVELS = 7
INSTR = 8
EXIT = 9

SCREEN_W = 800
SCREEN_H = 600

GRID_W = 10
GRID_H = 10

TILE_SIZE = 40
TILE_GAP = 4
TILE_START = (int((SCREEN_W - GRID_W * TILE_SIZE) / 2), int((SCREEN_H - GRID_H * TILE_SIZE) / 2))
TILE_END = (int(TILE_START[0] + GRID_W * TILE_SIZE), int(TILE_START[1] + GRID_H * TILE_SIZE))
TILESTACK_LOCATION = [(SCREEN_W - GRID_W * TILE_SIZE)/4 - TILE_SIZE, SCREEN_H/2 - TILE_SIZE/2]

MENU_BUTTON_W = 300
MENU_BUTTON_H = 100
MENU_BUTTON_GAP = 20
MENU_START = ((SCREEN_W - MENU_BUTTON_W) / 2, (SCREEN_H - MENU_BUTTON_H * 3 - MENU_BUTTON_GAP * 2) / 2)

LEVEL_BUTTON_SIZE = 150
LEVEL_BUTTON_GAP = 25
LEVEL_START = ((SCREEN_W - 3 * LEVEL_BUTTON_SIZE - 2 * LEVEL_BUTTON_GAP) / 2,
               (SCREEN_H - 2 * LEVEL_BUTTON_SIZE - LEVEL_BUTTON_GAP) / 2)

BG_COLOR = (30, 30, 30)
TILE_UNOCCUPIED_COLOR = (100, 100, 100)
TILE_OCCUPIED_COLOR = (200, 200, 200)
LAZOR_COLOR = (225, 20, 40)
CHECKPOINT_COLOR = (150, 150, 150)
DOT_COLOR = (225, 134, 143)

LAZORHEAD_RADIUS = 10
LAZOR_THICKNESS = 7

# Laser ray direction
NW = 1
NE = 2
SE = 3
SW = 4

RAY_ENDLESS = 0
RAY_ENDING = 1

LVL1 = {"LAZOR_SPAWN": [8.5, 1], "LAZOR_DIR": SW, "TILES": 5, "CHECKPOINTS": [[2, 2.5], [2.5, 3], [3, 3.5]]}
LVL2 = {"LAZOR_SPAWN": [4, 5.5], "LAZOR_DIR": NW, "TILES": 7, "CHECKPOINTS": [[4, 2.5], [2.5, 5], [8, 3.5]]}
LVL3 = {"LAZOR_SPAWN": [1, 1.5], "LAZOR_DIR": NE, "TILES": 3, "CHECKPOINTS": [[4, 1.5], [5, 5.5], [2, 3.5]]}
LVL4 = {"LAZOR_SPAWN": [9.5, 9], "LAZOR_DIR": SE, "TILES": 4, "CHECKPOINTS": [[4, 8.5], [5, 2.5], [6.5, 3]]}
LVL5 = {"LAZOR_SPAWN": [0.5, 1], "LAZOR_DIR": SE, "TILES": 2, "CHECKPOINTS": [[4, 7.5], [0.5, 4], [8, 1.5]]}
LVLRAND = {"LAZOR_SPAWN": [3.5, 4], "LAZOR_DIR": NE}

# TODO: fix endless ray bug, also with start in spawn location
# TODO: Show instructions
# TODO: Actual levels
# TODO: Winning the level (all laserpoints passed)
