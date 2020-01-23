import sys
import pygame

SCRIPT_PATH = sys.path[0]

SCREENWIDTH = 1344
# SCREENWIDTH = 960
SCREENHEIGHT = 728
# SCREENHEIGHT = 540
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

TILE_WIDTH = TILE_HEIGHT = int(SCREENWIDTH * 0.05)

# Colors
GREEN = (255, 0, 0)
RED = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Joystick
JS_XAXIS = 0  # axis 0 for left/right (default for most joysticks)
JS_YAXIS = 1  # axis 1 for up/down (default for most joysticks)

# PLayers
NUM_OF_PLAYERS = 4
PLAYERS = {
    0: {
        "COLOR": YELLOW,
        "PHYSICAL_POSITION": (0, 0),
        "KEY_INPUT": {"Down": pygame.K_DOWN, "Up": pygame.K_UP, "Left": pygame.K_LEFT, "Right": pygame.K_RIGHT},
        "START_POSITION": (SCREENWIDTH * 0.25, SCREENHEIGHT * 0.25)
    },
    1: {
        "COLOR": GREEN,
        "PHYSICAL_POSITION": (0, SCREENHEIGHT),
        "KEY_INPUT": {"Down": pygame.K_s, "Up": pygame.K_w, "Left": pygame.K_a, "Right": pygame.K_d},
        "START_POSITION": (SCREENWIDTH * 0.25, SCREENHEIGHT * 0.75)
    },
    2: {
        "COLOR": RED,
        "PHYSICAL_POSITION": (SCREENWIDTH, 0),
        "KEY_INPUT": {"Down": pygame.K_g, "Up": pygame.K_t, "Left": pygame.K_f, "Right": pygame.K_h},
        "START_POSITION": (SCREENWIDTH * 0.75, SCREENHEIGHT * 0.25)
    },
    3: {
        "COLOR": BLUE,
        "PHYSICAL_POSITION": (SCREENWIDTH, SCREENHEIGHT),
        "KEY_INPUT": {"Down": pygame.K_k, "Up": pygame.K_i, "Left": pygame.K_j, "Right": pygame.K_l},
        "START_POSITION": (SCREENWIDTH * 0.75, SCREENHEIGHT * 0.75)
    }
}