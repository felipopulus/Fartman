import os
from pygame.locals import QUIT

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