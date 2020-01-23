import os
from gameConstants import *


class game(object):

    PYGAME = None

    @classmethod
    def setPyGame(cls, pygame):
        cls.PYGAME = pygame

    def __init__(self, pygame, players=None, level=None):
        self.setPyGame(pygame)

        self.levelNum = 0
        self.score = 0
        self.lives = 3

        self.players = players
        self.level = level

        # game "mode" variable
        # 1 = normal
        # 2 = hit ghost
        # 3 = game over
        # 4 = wait to start
        # 5 = wait after eating ghost
        # 6 = wait after finishing level
        self.mode = 0
        self.modeTimer = 0
        self.ghostTimer = 0
        self.ghostValue = 0
        self.fruitTimer = 0
        self.fruitScoreTimer = 0
        self.fruitScorePos = (0, 0)

        self.SetMode(3)

        # camera variables
        self.screenPixelPos = (0, 0)  # absolute x,y position of the screen from the upper-left corner of the level
        self.screenNearestTilePos = (0, 0)  # nearest-tile position of the screen from the UL corner
        self.screenPixelOffset = (0, 0)  # offset in pixels of the screen from its nearest-tile position

        self.screenSize = SCREENSIZE
        self.screenTileSize = (self.screenSize[0] / int(TILE_WIDTH), self.screenSize[1] / int(TILE_HEIGHT))

        # numerical display digits
        self.digit = {}
        for i in range(0, 10, 1):
            self.digit[i] = self.PYGAME.image.load(os.path.join(SCRIPT_PATH, "res", "text", str(i) + ".gif")).convert()
        self.imLife = self.PYGAME.image.load(os.path.join(SCRIPT_PATH, "res", "text", "life.gif")).convert()
        self.imGameOver = self.PYGAME.image.load(os.path.join(SCRIPT_PATH, "res", "text", "gameover.gif")).convert()
        self.imReady = self.PYGAME.image.load(os.path.join(SCRIPT_PATH, "res", "text", "ready.gif")).convert()
        self.imLogo = self.PYGAME.image.load(os.path.join(SCRIPT_PATH, "res", "text", "logo.gif")).convert()
        # self.imHiscores = self.makehiscorelist()

    def SetMode(self, newMode):
        self.mode = newMode
        self.modeTimer = 0

    def SetPlayers(self, players):
        self.players = players

    def SetLevel(self, level):
        self.level = level

    def GetLevelNum(self):
        return self.levelNum

    def StartNewGame(self):
        self.levelNum = 1
        self.score = 0
        self.lives = 3

        self.SetMode(4)
        self.level.LoadLevel(self.GetLevelNum())


if __name__ == "__main__":
    import pygame
    pygame.init()
    pygame.display.set_mode(SCREENSIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Test gameFactory.py")
    game_obj = game(pygame)
    print game_obj