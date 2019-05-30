import re
from itertools import cycle


class Connect4():
    _WIDTH = 7
    _HEIGHT = 6
    _WIN_CONDITIONS = [re.compile(pattern) for pattern in map(r'([12])(.{{{}}}\1){{3}}'.format, (0, 5, 6, 7))]

    def __init__(self):
        self.board = ['' for __ in range(Connect4._WIDTH)]
        self.players = cycle('12')
        self.done = False

    def winner(self):
        board_state = '_'.join(row.ljust(Connect4._HEIGHT) for row in self.board)
        return any(pattern.search(board_state) for pattern in Connect4._WIN_CONDITIONS)

    def play(self, col):
        if self.done:
            return 'Game has finished!'
        if len(self.board[col]) == Connect4._HEIGHT:
            return 'Column full!'
        current_player = next(self.players)
        self.board[col] += current_player
        if self.winner():
            self.done = True
            return 'Player {} wins!'.format(current_player)
        return 'Player {} has a turn'.format(current_player)