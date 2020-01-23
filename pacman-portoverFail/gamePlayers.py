import os
from gameConstants import *


class pacman():

    pygame = None

    @classmethod
    def setPyGame(cls, pygame):
        cls.pygame = pygame

    def __init__(self, pygame):
        self.setPyGame(pygame)
        self.game = None
        
        self.x = 0
        self.y = 0
        self.velX = 0
        self.velY = 0
        self.speed = 3

        self.nearestRow = 0
        self.nearestCol = 0

        self.homeX = 0
        self.homeY = 0

        self.anim_pacmanL = {}
        self.anim_pacmanR = {}
        self.anim_pacmanU = {}
        self.anim_pacmanD = {}
        self.anim_pacmanS = {}
        self.anim_pacmanCurrent = {}

        for i in range(1, 9, 1):
            self.anim_pacmanL[i] = self.pygame.image.load(
                os.path.join(SCRIPT_PATH, "res", "sprite", "pacman-l " + str(i) + ".gif")).convert()
            self.anim_pacmanR[i] = self.pygame.image.load(
                os.path.join(SCRIPT_PATH, "res", "sprite", "pacman-r " + str(i) + ".gif")).convert()
            self.anim_pacmanU[i] = self.pygame.image.load(
                os.path.join(SCRIPT_PATH, "res", "sprite", "pacman-u " + str(i) + ".gif")).convert()
            self.anim_pacmanD[i] = self.pygame.image.load(
                os.path.join(SCRIPT_PATH, "res", "sprite", "pacman-d " + str(i) + ".gif")).convert()
            self.anim_pacmanS[i] = self.pygame.image.load(os.path.join(SCRIPT_PATH, "res", "sprite", "pacman.gif")).convert()

        self.pelletSndNum = 0

    def SetGame(self, game):
        self.game = game
        
    def Move(self):

        self.nearestRow = int(((self.y + (TILE_WIDTH / 2)) / TILE_WIDTH))
        self.nearestCol = int(((self.x + (TILE_HEIGHT / 2)) / TILE_HEIGHT))

        self.x += self.velX
        self.y += self.velY


if __name__ == "__main__":
    import pygame
    pygame.init()
    pygame.display.set_mode(SCREENSIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
    pygame.display.set_caption("Test gamePlayers.py")
    pacman_obj = pacman(pygame)
    pacman_obj.Move()