pygame = None


def setPyGame(__pygame):
    global pygame
    pygame = __pygame


class level(object):
    def __init__(self):
        self.__game = None
        self.__players = None

    @property
    def game(self):
        return self.__game

    @game.setter
    def game(self, game):
        self.__game = game

    @property
    def players(self):
        return self.__game.players
