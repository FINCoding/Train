import re


class Connect4:
    def __init__(self):
        self.cols = [[0] * 6 for _ in range(7)]
        self.next_player = 1

    def play(self, col):
        assert 0 <= col <= 6
        if not self.next_player:
            return "Game has finished!"
        if self.cols[col][-1]:
            return "Column full!"
        row = next(row for row in range(6) if not self.cols[col][row])
        self.cols[col][row] = self.next_player
        board_str = "\n".join("".join(map(str, col)) for col in self.cols)
        if self.is_finished(board_str):
            result = "Player {} wins!".format(self.next_player)
            self.next_player = 0
        else:
            result = "Player {} has a turn".format(self.next_player)
            self.next_player = {1: 2, 2: 1}[self.next_player]
        return result

    is_finished = re.compile(
        r"([12])"
        r"(?:"
            r"\1{3}|"
            r"(?:.{5}\1){3}|"
            r"(?:.{6}\1){3}|"
            r"(?:.{7}\1){3}"
        r")", re.DOTALL).search