import re

class Connect4:

    COLUMNS = 7
    ROWS = 6

    def __init__(self):
        self._board = [[0] * Connect4.COLUMNS for row in range(Connect4.ROWS)]
        self._player = 1
        self._done = False
        self._height = [0] * Connect4.COLUMNS

    def __repr__(self):
        flat_list = [str(item) for sublist in self._board for item in sublist]
        return "".join("-" + str(e) if i % 7 == 0 and i != 0 else str(e) for i, e in enumerate(flat_list))

    def drop_into_column(self, column):
        if self._height[column] == 6:
            return False
        else:
            self._board[self._height[column]][column] = self._player
            self._height[column] += 1
            return True

    def check_win_condition(self):
        board = self.__repr__()
        return re.search(r'([12])(?:\1{3}|(?:.{6}\1){3}|(?:.{7}\1){3}|(?:.{8}\1){3})', board)

    def play(self, column):
        if self._done:
            return "Game has finished!"
        if not self.drop_into_column(column):
            return "Column full!"
        else:
            if self.check_win_condition():
                self._done = True
                return "Player %d wins!" % self._player
            else:
                turn_message = "Player %d has a turn" % self._player
                if self._player == 1:
                    self._player = 2
                else:
                    self._player = 1
                return turn_message