class Connect4():
    EMPTY = "."

    def __init__(self):
        # set up empty grid and variables
        self.grid = [[self.EMPTY] * 7 for _ in range(6)]
        self.player = 1
        self.game_over = False

    def check(self, lines):
        # check if there are four in line
        for line in lines:
            line = "".join(map(str, line))
            found = max(line.find("1111"), line.find("2222"))
            if found >= 0:
                return True

    def diagonals(self):
        # generate diagonals from grid
        right, left = [], []
        for i, row in enumerate(self.grid):
            right.append([self.EMPTY] * i + row + [self.EMPTY] * (5 - i))
            left.append([self.EMPTY] * (5 - i) + row + [self.EMPTY] * i)
        return list(zip(*right)) + list(zip(*left))

    def play(self, column):
        # when game is over
        if self.game_over:
            return "Game has finished!"

        # get current player
        current = self.player

        # place the disc
        for row in range(6):
            if self.grid[row][column] == self.EMPTY:
                self.grid[row][column] = current
                break
        # or if column is full
        else:
            return "Column full!"

        # check for winner
        winner = self.check(self.grid) or self.check(zip(*self.grid)) or self.check(self.diagonals())
        if winner:
            self.game_over = True
            return "Player %s wins!" % current

        # otherwise next player
        self.player = 3 - current
        return "Player %s has a turn" % current

if __name__ == '__main__':
    game = Connect4()
    # print(game)
    print(game.play(4))
    print(game.play(4))
    print(game.play(4))
    print(game.play(4))
    print(game.play(4))
    print(game.play(4))
    print(game.play(4))
    print(game.play(3))
    print(game.play(3))