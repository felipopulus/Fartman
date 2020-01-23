import os
from pacConstants import *
import pygame


def setPyGame(__pygame):
    global pygame
    pygame = __pygame


class pacman(pygame.sprite.Sprite):
    def __init__(self, id):

        pygame.sprite.Sprite.__init__(self)

        self.__id = id
        self.__game = None
        self.physicalPosition = PLAYERS[id]["PHYSICAL_POSITION"]

        # Inputs
        self.__keyboard = PLAYERS[id]["KEY_INPUT"]
        self.__joystick = None
        self.initJoystick(id)

        # Player Params
        self.__speed = 5
        self.__velX = 0
        self.__velY = 0
        self.__color = PLAYERS[id]["COLOR"]

        # Sprites
        spriteLocation = os.path.join(SCRIPT_PATH, "res", "sprite")
        self.animFrame = 1
        self.anim_pacmanL = {}
        self.anim_pacmanR = {}
        self.anim_pacmanU = {}
        self.anim_pacmanD = {}
        self.anim_pacmanS = {}
        for i in range(1, 9, 1):
            self.anim_pacmanL[i] = pygame.image.load(
                os.path.join(spriteLocation, "pacman-l " + str(i) + ".gif")).convert()
            self.anim_pacmanR[i] = pygame.image.load(
                os.path.join(spriteLocation, "pacman-r " + str(i) + ".gif")).convert()
            self.anim_pacmanU[i] = pygame.image.load(
                os.path.join(spriteLocation, "pacman-u " + str(i) + ".gif")).convert()
            self.anim_pacmanD[i] = pygame.image.load(
                os.path.join(spriteLocation, "pacman-d " + str(i) + ".gif")).convert()
            self.anim_pacmanS[i] = pygame.image.load(os.path.join(spriteLocation, "pacman.gif")).convert()
        self.image = self.anim_pacmanS[1]
        # dest = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
        # self.image = pygame.transform.scale(self.image, (TILE_WIDTH, TILE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = PLAYERS[id]["START_POSITION"][0]
        self.rect.y = PLAYERS[id]["START_POSITION"][1]
        self.__width = self.image.get_width()
        self.__height = self.image.get_height()

    @property
    def game(self):
        return self.game

    @game.setter
    def game(self, game):
        self.__game = game

    @property
    def level(self):
        return self.__game.level

    @property
    def keyboard(self):
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, keyboard):
        self.__keyboard = keyboard

    @property
    def keyRight(self):
        return self.__keyboard["Right"]

    @property
    def keyLeft(self):
        return self.__keyboard["Left"]

    @property
    def keyUp(self):
        return self.__keyboard["Up"]

    @property
    def keyDown(self):
        return self.keyboard["Down"]

    @property
    def joystick(self):
        return self.__joystick

    @joystick.setter
    def joystick(self, joystick):
        self.__joystick = joystick

    def initJoystick(self, identifier):
        if identifier < pygame.joystick.get_count():
            self.joystick = pygame.joystick.Joystick(identifier)
            self.joystick.init()
        else:
            print("No joystick available for identifier: {}".format(identifier))

    @property
    def speed(self):
        return self.__speed

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def velX(self):
        return self.__velX

    @velX.setter
    def velX(self, velX):
        self.__velX = velX

    @property
    def velY(self):
        return self.__velY

    @velY.setter
    def velY(self, velY):
        self.__velY = velY

    def processInputs(self):
        if self.__game.mode == "GamePlay":
            if pygame.key.get_pressed()[self.keyRight] or (self.__joystick and self.__joystick.get_axis(JS_XAXIS) > 0.5):
                if not (self.velX == self.speed and self.velY == 0):
                    print("Player {}: right".format(self.__id))
                    self.velX = self.speed
                    self.velY = 0

            elif pygame.key.get_pressed()[self.keyLeft] or (self.__joystick and self.__joystick.get_axis(JS_XAXIS) < -0.5):
                if not (self.velX == -self.speed and self.velY == 0):
                    print("Player {}: left".format(self.__id))
                    self.velX = -self.speed
                    self.velY = 0

            elif pygame.key.get_pressed()[self.keyDown] or (self.__joystick and self.__joystick.get_axis(JS_YAXIS) > 0.5):
                if not (self.velX == 0 and self.velY == self.speed):
                    print("Player {}: down".format(self.__id))
                    self.velX = 0
                    self.velY = self.speed

            elif pygame.key.get_pressed()[self.keyUp] or (self.__joystick and self.__joystick.get_axis(JS_YAXIS) < -0.5):
                if not (self.velX == 0 and self.velY == -self.speed):
                    print("Player {}: up".format(self.__id))
                    self.velX = 0
                    self.velY = -self.speed

    def checkPlayerCollitions(self):
        collition_group = [x for x in self.__game.players if x != self]
        collision_list = pygame.sprite.spritecollide(self, collition_group, False)
        if collision_list:
            self.velX = -self.velX
            self.velY = -self.velY

    def Move(self):
        self.rect.x += self.velX
        self.rect.y += self.velY

        self.checkPlayerCollitions()

        # Collisions
        rightEdge = SCREENWIDTH - self.__width
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= rightEdge:
            self.rect.x = rightEdge

        bottomEdge = SCREENHEIGHT - self.__height
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= bottomEdge:
            self.rect.y = bottomEdge

    def updateSprites(self):
        # set the current frame array to match the direction pacman is facing
        current = self.anim_pacmanS
        if self.velX > 0:
            current = self.anim_pacmanR
        elif self.velX < 0:
            current = self.anim_pacmanL
        elif self.velY > 0:
            current = self.anim_pacmanD
        elif self.velY < 0:
            current = self.anim_pacmanU
        self.image = current[self.animFrame]

        # pygame.draw.rect(self.image, self.__color, [0, 0, self.__width, self.__height])

        if self.__game.mode == "GamePlay":
            if not self.velX == 0 or not self.velY == 0:
                # only Move mouth when pacman is moving
                self.animFrame += 1

            if self.animFrame == 9:
                # wrap to beginning
                self.animFrame = 1

