

class cl_path_finder:
    def __init__(self, maze):
        self.maze = maze.split('\n')
        self.index_checked = []
        self.start = cl_node(0,0)
        self.wall = 'W'
        self.exit = cl_node(len(self.maze)-1, self.get_len_row(self.maze[0])-1)
        self.Finded = False

    def get_len_row(self, row):
        return len(row)

    def get_up_neighbour(self, node):
        new_row = node.row - 1
        if new_row >= 0 and self.maze[new_row][node.index] != self.wall:
           return cl_node(new_row, node.index)
        return False
    #
    def get_down_neighbour(self, node):
        new_row = node.row + 1
        if new_row <= self.exit.row and self.maze[new_row][node.index] != self.wall:
           return cl_node(new_row, node.index)
        return False
    #
    def get_left_neighbour(self, node):
        new_ind = node.index - 1
        if new_ind >= 0 and self.maze[node.row][new_ind] != self.wall:
            return cl_node(node.row, new_ind)
        return False
    #
    def get_right_neighbour(self, node):
        new_ind = node.index + 1
        if new_ind <= self.exit.index and self.maze[node.row][new_ind] != self.wall:
           return cl_node(node.row, new_ind)
        return False

    def parse_maze(self, node):

        while True and self.Finded == False:
            if node.id == self.exit.id: self.Finded = True
            if node.id in self.index_checked: break

            self.index_checked.append(node.id)

            up_neighbour = self.get_up_neighbour(node)
            if up_neighbour: self.parse_maze(up_neighbour)

            down_neighbour = self.get_down_neighbour(node)
            if down_neighbour: self.parse_maze(down_neighbour)

            right_neighbour = self.get_right_neighbour(node)
            if right_neighbour: self.parse_maze(right_neighbour)

            left_neighbour = self.get_left_neighbour(node)
            if left_neighbour: self.parse_maze(left_neighbour)

        return self.Finded

    def run(self):
        return self.parse_maze(self.start)

    # def exit_is_possible(self):
    #     return self.index_checked.get(self.exit.row) == self.exit.index

class cl_node:
    def __init__(self, row, index):
        self.row = row
        self.index = index
        self.id = str(row)+str(index)

def path_finder(maze):
    lo = cl_path_finder(maze)
    print(lo.run())
    # print(lo.is_it_exit(1))

if __name__ == '__main__':
    a = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])

    d = "\n".join([
        "......",
        "......",
        "......",
        "......",
        ".....W",
        "....W."
    ])
    path_finder(d)