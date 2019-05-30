class Connect4():

    def __init__(self):
        self.grid = [[0]*7 for i in range(6)]
        self.player_move = 1
        self.won = False

    def __str__(self):
        return ("Player %d has a turn" % self.player_move)

    def check_column_is_full(self, col):
        return self.grid[len(self.grid)-1][col] != 0

    def play(self, col):
        if self.won: return "Game has finished!"
        if self.check_column_is_full(col): return 'Column full!'
        row, whose_turn = self.put_disk(col)
        if self.is_won(col,row):
            self.won = True
            # current_player = self.player_move
            # self.next_player()
            return ('Player %d wins!' % self.player_move)
        self.next_player()
        return whose_turn

    def put_disk(self,col):
        for row in range(len(self.grid)):
            if self.grid[row][col] == 0:
                self.grid[row][col] = self.player_move
                return row,self.__str__()

    def next_player(self):
        if self.player_move == 1: self.player_move = 2
        else: self.player_move = 1

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= y < len(self.grid) and 0 <= x < len(self.grid[0])

    def is_won(self,x,y):
        finish_dot_of_lines = [(x,y+3),(x,y-3),(x+3,y),(x-3,y),
                             (x+3,y+3),(x-3,y-3),(x-3,y+3),(x+3,y-3)]
        finisch_dot_lines = filter(self.in_bounds, finish_dot_of_lines)
        for i in finisch_dot_lines:
            if self.check_line_is_won(x,y,i): return True

    def check_line_is_won(self,x,y,id):
        (x_fin, y_fin) = id
        while x!=x_fin or y!=y_fin:
            disk_pre = self.grid[y][x]
            if y_fin > y: y += 1
            elif y_fin < y: y -= 1
            if x_fin > x: x += 1
            elif x_fin < x: x -= 1
            disk_new = self.grid[y][x]
            if disk_pre != disk_new: return False
        return True

        




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
    # print(game.play(5))
    # print(game.play(5))
    # print(game.play(5))