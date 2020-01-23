import pygame
from gameConstants import *
import gameFactory as gf
import gameUtils as gu
import gamePlayers as gp
import gameLevels as gl


# Start Game
pygame.init()

# Game essentials
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREENSIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("4-Pacman")
gu.setPyGame(pygame)

# Create the pacmen
player1 = gp.pacman(pygame)
player2 = gp.pacman(pygame)
players = [player1, player2]

# Load Levels
thisLevel = gl.level(pygame)

# Instantiate Game Objects
thisGame = gf.game(pygame)
thisGame.SetLevel(thisLevel)
thisGame.SetPlayers(players)

# Set the game object in all other game objects
for player in players:
    player.SetGame(thisGame)
thisLevel.SetGame(thisGame)

thisGame.StartNewGame()


def CheckInputs():
    for player in players:
        if thisGame.mode == 1:
            if pygame.key.get_pressed()[pygame.K_RIGHT]: # or (js != None and js.get_axis(JS_XAXIS) > 0.5):
                if not (player.velX == player.speed and player.velY == 0):
                    player.velX = player.speed
                    player.velY = 0

            elif pygame.key.get_pressed()[pygame.K_LEFT]: # or (js != None and js.get_axis(JS_XAXIS) < -0.5):
                if not (player.velX == -player.speed and player.velY == 0):
                    player.velX = -player.speed
                    player.velY = 0

            elif pygame.key.get_pressed()[pygame.K_DOWN]: # or (js != None and js.get_axis(JS_YAXIS) > 0.5):
                if not (player.velX == 0 and player.velY == player.speed):
                    player.velX = 0
                    player.velY = player.speed

            elif pygame.key.get_pressed()[pygame.K_UP]: # or (js != None and js.get_axis(JS_YAXIS) < -0.5):
                if not (player.velX == 0 and player.velY == -player.speed):
                    player.velX = 0
                    player.velY = -player.speed

        elif thisGame.mode == 3:
            if pygame.key.get_pressed()[pygame.K_RETURN]: # or (js != None and js.get_button(JS_STARTBUTTON)):
                thisGame.StartNewGame()


while True:

    # Check if player has quit the game
    if gu.CheckIfCloseButton(pygame.event.get()):
        pygame.quit()

    if thisGame.mode == 1:
        # normal gameplay mode
        CheckInputs()

        thisGame.modeTimer += 1
        for player in players:
            player.Move()
        # for i in range(0, 4, 1):
        #     ghosts[i].Move()
        # thisFruit.Move()