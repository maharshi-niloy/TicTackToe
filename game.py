import time
from TickTackToe.player import Human, Computer


class TicTakToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_winner = None

    @staticmethod
    def print_num_board():
        number_board = [[str(i) for i in range(i*3, (i+1)*3)] for i in range(3)]
        for row in number_board:
            print('| ', ' | '.join(row), ' |')

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ', ' | '.join(row), ' |')

    def available_moves(self):
        return [count for count, symbol in enumerate(self.board) if symbol == ' ']

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all(symbol == letter for symbol in row):
            return True

        col_ind = square % 3
        col = [self.board[col_ind+i*3] for i in range(3)]
        if all(symbol == letter for symbol in col):
            return True

        diagonal1 = [self.board[i] for i in [0, 4, 8]]
        if all(symbol == letter for symbol in diagonal1):
            return True
        diagonal2 = [self.board[i] for i in [2, 4, 6]]
        if all(symbol == letter for symbol in diagonal2):
            return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_num_board()

    letter = 'x'
    while ' ' in game.board:
        if letter == 'x':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter, 'made a move to', square)
                game.print_board()
                print(' ')

        if game.current_winner is not None:
            if print_game:
                print(letter, 'wins!')
            return letter

        letter = 'o' if letter == 'x' else 'x'
        time.sleep(.8)

    if print_game:
        print('It\'s a tie.')


if __name__ == '__main__':
    x_player = Human('x')
    o_player = Computer('o')
    t = TicTakToe()
    play(t, x_player, o_player, print_game=True)

