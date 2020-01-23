pygame = None


def setPyGame(__pygame):
    global pygame
    pygame = __pygame


class game(object):
    def __init__(self):
        self.__mode = "GamePlay"
        self.__level = None
        self.__players = None

        self.screen = pygame.display.get_surface()

    @property
    def mode(self):
        return self.__mode

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    def startNewGame(self):
        print("Start new Game")


