class Connect4:

    def __init__(self, players='12', width=7, height=6):
        self.turn, self.players, self.grid = 0, players, [[' '] * height for _ in range(width)]

    def play(self, col):
        if self.turn is None:
            return 'Game has finished!'

        # Plays a turn
        try:
            self.grid[col][self.grid[col].index(' ')] = self.players[self.turn]
        except:
            return 'Column full!'
        previous_player, self.turn = self.turn, (self.turn + 1) % len(self.players)

        # Checks if there is a winner
        line = [None] * (len(self.grid) - 1)
        if any(self.players[previous_player] * 4 in ' '.join(map(''.join, g)) for g in (
            self.grid,       ## Horizontal
            zip(*self.grid), ## Vertical
            (filter(None, r) for r in zip(*(line[i:] + c + line[:i] for i, c in enumerate(self.grid)))), ## Diagonal forward
            (filter(None, r) for r in zip(*(line[:i] + c + line[i:] for i, c in enumerate(self.grid))))  ## Diagonal backward
        )):
            self.turn = None
            return 'Player %s wins!' % self.players[previous_player]

        return 'Player %s has a turn' % self.players[previous_player]