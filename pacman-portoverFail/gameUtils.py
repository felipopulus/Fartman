import os
from pygame.locals import QUIT
from gameConstants import *

pygame = None

tileIDName = {}  # gives tile name (when the ID# is known)
tileID = {}  # gives tile ID (when the name is known)
tileIDImage = {}  # gives tile image (when the ID# is known)


def setPyGame(__pygame):
    global pygame
    pygame = __pygame


def CheckIfCloseButton(events):
    for event in events:
        if event.type == QUIT:
            return True
    return False

#      _____________________________________________
# ___/  function: Get ID-Tilename Cross References  \______________________________________

def GetCrossRef():
    f = open(os.path.join(SCRIPT_PATH, "res", "crossref.txt"), 'r')

    lineNum = 0
    useLine = False

    for i in f.readlines():
        # print " ========= Line " + str(lineNum) + " ============ "
        while len(i) > 0 and (i[-1] == '\n' or i[-1] == '\r'): i = i[:-1]
        while len(i) > 0 and (i[0] == '\n' or i[0] == '\r'): i = i[1:]
        str_splitBySpace = i.split(' ')

        j = str_splitBySpace[0]

        if (j == "'" or j == "" or j == "#"):
            # comment / whitespace line
            # print " ignoring comment line.. "
            useLine = False
        else:
            # print str(wordNum) + ". " + j

            useLine = True

        if useLine == True:
            tileIDName[int(str_splitBySpace[0])] = str_splitBySpace[1]
            tileID[str_splitBySpace[1]] = int(str_splitBySpace[0])

            thisID = int(str_splitBySpace[0])
            if not thisID in NO_GIF_TILES:
                tileIDImage[thisID] = pygame.image.load(os.path.join(SCRIPT_PATH, "res", "tiles", str_splitBySpace[1] + ".gif")).convert()
            else:
                tileIDImage[thisID] = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))

            # change colors in tileIDImage to match maze colors
            for y in range(0, TILE_WIDTH, 1):
                for x in range(0, TILE_HEIGHT, 1):

                    if tileIDImage[thisID].get_at((x, y)) == IMG_EDGE_LIGHT_COLOR:
                        # wall edge
                        tileIDImage[thisID].set_at((x, y), thisLevel.edgeLightColor)

                    elif tileIDImage[thisID].get_at((x, y)) == IMG_FILL_COLOR:
                        # wall fill
                        tileIDImage[thisID].set_at((x, y), thisLevel.fillColor)

                    elif tileIDImage[thisID].get_at((x, y)) == IMG_EDGE_SHADOW_COLOR:
                        # pellet color
                        tileIDImage[thisID].set_at((x, y), thisLevel.edgeShadowColor)

                    elif tileIDImage[thisID].get_at((x, y)) == IMG_PELLET_COLOR:
                        # pellet color
                        tileIDImage[thisID].set_at((x, y), thisLevel.pelletColor)

        # print str_splitBySpace[0] + " is married to " + str_splitBySpace[1]
        lineNum += 1