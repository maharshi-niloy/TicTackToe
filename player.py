import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        square = None
        while not valid_square:
            val = input(self.letter + '\'s move. Input move(0-8): ')
            try:
                square = int(val)
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return square


class Computer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
