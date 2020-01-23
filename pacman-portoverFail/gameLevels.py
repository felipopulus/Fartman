import os
import random
from gameConstants import *
import gameUtils as gu


class level(object):

    pygame = None

    @classmethod
    def setPyGame(cls, pygame):
        cls.pygame = pygame

    def __init__(self, pygame):
        self.setPyGame(pygame)
        self.game = None

        self.lvlWidth = 0
        self.lvlHeight = 0
        self.edgeLightColor = (255, 255, 0, 255)
        self.edgeShadowColor = (255, 150, 0, 255)
        self.fillColor = (0, 255, 255, 255)
        self.pelletColor = (255, 255, 255, 255)

        self.map = {}

        self.pellets = 0
        self.powerPelletBlinkTimer = 0
        
    def SetGame(self, game):
        self.game = game

    def SetMapTile(self, (row, col), newValue):
        self.map[(row * self.lvlWidth) + col] = newValue

    def GetMapTile(self, (row, col)):
        if row >= 0 and row < self.lvlHeight and col >= 0 and col < self.lvlWidth:
            return self.map[(row * self.lvlWidth) + col]
        else:
            return 0

    def IsWall(self, (row, col)):

        if row > self.lvlHeight - 1 or row < 0:
            return True

        if col > self.lvlWidth - 1 or col < 0:
            return True

        # check the offending tile ID
        result = self.GetMapTile((row, col))

        # if the tile was a wall
        if result >= 100 and result <= 199:
            return True
        else:
            return False

    def CheckIfHitWall(self, (possiblePlayerX, possiblePlayerY), (row, col)):

        numCollisions = 0

        # check each of the 9 surrounding tiles for a collision
        for iRow in range(row - 1, row + 2, 1):
            for iCol in range(col - 1, col + 2, 1):

                if (possiblePlayerX - (iCol * TILE_WIDTH) < TILE_WIDTH) and (
                        possiblePlayerX - (iCol * TILE_WIDTH) > -TILE_WIDTH) and (
                        possiblePlayerY - (iRow * TILE_HEIGHT) < TILE_HEIGHT) and (
                        possiblePlayerY - (iRow * TILE_HEIGHT) > -TILE_HEIGHT):

                    if self.IsWall((iRow, iCol)):
                        numCollisions += 1

        if numCollisions > 0:
            return True
        else:
            return False

    def CheckIfHit(self, (playerX, playerY), (x, y), cushion):

        if (playerX - x < cushion) and (playerX - x > -cushion) and (playerY - y < cushion) and (
                playerY - y > -cushion):
            return True
        else:
            return False

    def CheckIfHitSomething(self, (playerX, playerY), (row, col)):
        return False

    def GetGhostBoxPos(self):
        return False

    def GetPathwayPairPos(self):
        return False

    def PrintMap(self):

        for row in range(0, self.lvlHeight, 1):
            outputLine = ""
            for col in range(0, self.lvlWidth, 1):
                outputLine += str(self.GetMapTile((row, col))) + ", "

            print outputLine

    def DrawMap(self):

        self.powerPelletBlinkTimer += 1
        if self.powerPelletBlinkTimer == 60:
            self.powerPelletBlinkTimer = 0

        for row in range(-1, self.game.screenTileSize[0] + 1, 1):
            outputLine = ""
            for col in range(-1, self.game.screenTileSize[1] + 1, 1):

                # row containing tile that actually goes here
                actualRow = self.game.screenNearestTilePos[0] + row
                actualCol = self.game.screenNearestTilePos[1] + col

                useTile = self.GetMapTile((actualRow, actualCol))
                # if not useTile == 0 and not useTile == tileID['door-h'] and not useTile == tileID['door-v']:
                #     # if this isn't a blank tile
                #
                #     if useTile == tileID['pellet-power']:
                #         if self.powerPelletBlinkTimer < 30:
                #             screen.blit(tileIDImage[useTile], (col * TILE_WIDTH - self.game.screenPixelOffset[0],
                #                                                row * TILE_HEIGHT - self.game.screenPixelOffset[1]))
                #
                #     elif useTile == tileID['showlogo']:
                #         screen.blit(self.game.imLogo, (col * TILE_WIDTH - self.game.screenPixelOffset[0],
                #                                       row * TILE_HEIGHT - self.game.screenPixelOffset[1]))
                #
                #     elif useTile == tileID['hiscores']:
                #         screen.blit(self.game.imHiscores, (col * TILE_WIDTH - self.game.screenPixelOffset[0],
                #                                           row * TILE_HEIGHT - self.game.screenPixelOffset[1]))
                #
                #     else:
                #         screen.blit(tileIDImage[useTile], (col * TILE_WIDTH - self.game.screenPixelOffset[0],
                #                                            row * TILE_HEIGHT - self.game.screenPixelOffset[1]))

    def LoadLevel(self, levelNum):

        self.map = {}

        self.pellets = 0

        f = open(os.path.join(SCRIPT_PATH, "res", "levels", str(levelNum) + ".txt"), 'r')
        lineNum = -1
        rowNum = 0
        useLine = False
        isReadingLevelData = False

        for line in f:

            lineNum += 1

            # print " ------- Level Line " + str(lineNum) + " -------- "
            while len(line) > 0 and (line[-1] == "\n" or line[-1] == "\r"): line = line[:-1]
            while len(line) > 0 and (line[0] == "\n" or line[0] == "\r"): line = line[1:]
            str_splitBySpace = line.split(' ')

            j = str_splitBySpace[0]

            if (j == "'" or j == ""):
                # comment / whitespace line
                # print " ignoring comment line.. "
                useLine = False
            elif j == "#":
                # special divider / attribute line
                useLine = False

                firstWord = str_splitBySpace[1]

                if firstWord == "lvlwidth":
                    self.lvlWidth = int(str_splitBySpace[2])
                # print "Width is " + str( self.lvlWidth )

                elif firstWord == "lvlheight":
                    self.lvlHeight = int(str_splitBySpace[2])
                # print "Height is " + str( self.lvlHeight )

                elif firstWord == "edgecolor":
                    # edge color keyword for backwards compatibility (single edge color) mazes
                    red = int(str_splitBySpace[2])
                    green = int(str_splitBySpace[3])
                    blue = int(str_splitBySpace[4])
                    self.edgeLightColor = (red, green, blue, 255)
                    self.edgeShadowColor = (red, green, blue, 255)

                elif firstWord == "edgelightcolor":
                    red = int(str_splitBySpace[2])
                    green = int(str_splitBySpace[3])
                    blue = int(str_splitBySpace[4])
                    self.edgeLightColor = (red, green, blue, 255)

                elif firstWord == "edgeshadowcolor":
                    red = int(str_splitBySpace[2])
                    green = int(str_splitBySpace[3])
                    blue = int(str_splitBySpace[4])
                    self.edgeShadowColor = (red, green, blue, 255)

                elif firstWord == "fillcolor":
                    red = int(str_splitBySpace[2])
                    green = int(str_splitBySpace[3])
                    blue = int(str_splitBySpace[4])
                    self.fillColor = (red, green, blue, 255)

                elif firstWord == "pelletcolor":
                    red = int(str_splitBySpace[2])
                    green = int(str_splitBySpace[3])
                    blue = int(str_splitBySpace[4])
                    self.pelletColor = (red, green, blue, 255)

                # elif firstWord == "fruittype":
                #     thisFruit.fruitType = int(str_splitBySpace[2])

                elif firstWord == "startleveldata":
                    isReadingLevelData = True
                    # print "Level data has begun"
                    rowNum = 0

                elif firstWord == "endleveldata":
                    isReadingLevelData = False
                # print "Level data has ended"

            else:
                useLine = True

            # this is a map data line
            if useLine == True:

                if isReadingLevelData == True:

                    # print str( len(str_splitBySpace) ) + " tiles in this column"

                    for k in range(0, self.lvlWidth, 1):
                        self.SetMapTile((rowNum, k), int(str_splitBySpace[k]))

                        thisID = int(str_splitBySpace[k])
                        if thisID == 4:
                            # starting position for pac-man

                            for player in self.game.players:
                                player.homeX = k * TILE_WIDTH
                                player.homeY = rowNum * TILE_HEIGHT
                                self.SetMapTile((rowNum, k), 0)

                        elif thisID >= 10 and thisID <= 13:
                            # one of the ghosts

                            # ghosts[thisID - 10].homeX = k * TILE_WIDTH
                            # ghosts[thisID - 10].homeY = rowNum * TILE_HEIGHT
                            self.SetMapTile((rowNum, k), 0)

                        elif thisID == 2:
                            # pellet

                            self.pellets += 1

                    rowNum += 1

        # reload all tiles and set appropriate colors
        gu.GetCrossRef()


        # # load map into the pathfinder object
        # path.ResizeMap((self.lvlHeight, self.lvlWidth))
        #
        # for row in range(0, path.size[0], 1):
        #     for col in range(0, path.size[1], 1):
        #         if self.IsWall((row, col)):
        #             path.SetType((row, col), 1)
        #         else:
        #             path.SetType((row, col), 0)
        #
        # # do all the level-starting stuff
        # self.Restart()

    def Restart(self):

        # for i in range(0, 4, 1):
        #     # move ghosts back to home
        #
        #     ghosts[i].x = ghosts[i].homeX
        #     ghosts[i].y = ghosts[i].homeY
        #     ghosts[i].velX = 0
        #     ghosts[i].velY = 0
        #     ghosts[i].state = 1
        #     ghosts[i].speed = 1
        #     ghosts[i].Move()
        #
        #     # give each ghost a path to a random spot (containing a pellet)
        #     (randRow, randCol) = (0, 0)
        #
        #     while not self.GetMapTile((randRow, randCol)) == tileID['pellet'] or (randRow, randCol) == (0, 0):
        #         randRow = random.randint(1, self.lvlHeight - 2)
        #         randCol = random.randint(1, self.lvlWidth - 2)
        #
        #     # print "Ghost " + str(i) + " headed towards " + str((randRow, randCol))
        #     ghosts[i].currentPath = path.FindPath((ghosts[i].nearestRow, ghosts[i].nearestCol), (randRow, randCol))
        #     ghosts[i].FollowNextPathWay()
        #
        # thisFruit.active = False
        #
        # self.game.fruitTimer = 0

        for player in self.game.players:
            player.x = self.game.player.homeX
            player.y = self.game.player.homeY
            player.velX = 0
            player.velY = 0

            player.anim_pacmanCurrent = self.game.player.anim_pacmanS
            player.animFrame = 3



if __name__ == "__main__":
    level_obj = level()
    level_obj.PrintMap()