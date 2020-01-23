
from pacConstants import *
import pacGame
import pacPlayer
import pacLevel
import pacUtils

# Start Game
pygame.init()

# Game essentials
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREENSIZE, pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("4-Pacman")

# make the same pygame instance available to all the modules
pacUtils.setPyGame(pygame)
pacGame.setPyGame(pygame)
pacPlayer.setPyGame(pygame)
pacLevel.setPyGame(pygame)

# Create the pacmen
players = pygame.sprite.Group()

# comment this line out for a set number of players
# NUM_OF_PLAYERS = pygame.joystick.get_count()
# TODO: replace NUM_OF_PLAYERS with unique player from start screen
for index in range(NUM_OF_PLAYERS):
    player = pacPlayer.pacman(index)
    players.add(player)
print "NUM_OF_PLAYERS", NUM_OF_PLAYERS

# Load Levels
thisLevel = pacLevel.level()

# Instantiate Game Objects
thisGame = pacGame.game()
thisGame.level = thisLevel
thisGame.players = players

# Set the game object in all other game objects
for player in players:
    player.game = thisGame
thisLevel.game = thisGame

thisGame.startNewGame()


# def CheckInputs():
#     for player in players:
#         player.processInputs()
#
#     if thisGame.mode == 3:
#         if pygame.key.get_pressed()[pygame.K_RETURN]: # or (js != None and js.get_button(JS_STARTBUTTON)):
#             thisGame.StartNewGame()

carryOn = True
while carryOn:
    # Check if player has quit the game
    if pacUtils.CheckIfCloseButton(pygame.event.get()):
        carryOn = False

    if thisGame.mode == "GamePlay":
        # normal gameplay mode
        # CheckInputs()

        # Draw sequence
        screen.fill((0,0,0))

        # Players
        for player in players:
            player.processInputs()
            player.Move()
            player.updateSprites()
            lineStart = player.physicalPosition
            lineEnd = [player.rect.x + player.width*.5, player.rect.y + player.height*.5]
            pygame.draw.line(screen, player.color, lineStart, lineEnd, 1)
            pygame.draw.rect(screen, player.color, player.rect)
        players.draw(screen)  # Now let's draw all the sprites in one go.

        # Refresh Screen
        pygame.display.flip()

        # Number of frames per second e.g. 60
        clock.tick(120)

        # thisGame.modeTimer += 1
        # for player in players:
        #     player.Move()
        # for i in range(0, 4, 1):
        #     ghosts[i].Move()
        # thisFruit.Move()

pygame.quit()
