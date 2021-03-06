
class cl_maze:
    def __init__(self, maze):
        self.maze = maze.split('\n')
        self.wave_front = []
        self.visited = []
        self.start = (0, 0)
        self.finish = (len(self.maze) - 1, len(self.maze[len(self.maze) - 1]) - 1)
        self.exit = False
        self.wall = 'W'

    def exit_is_available(self):
        self.wave_front.append(self.start)
        self.visited.append(self.start)

        while len(self.wave_front) != 0:
            current = self.wave_front[0]
            self.wave_front.remove(current)
            if current == self.finish: return True

            for next in self.get_neighbours(current):
                if next not in self.visited:
                    self.wave_front.append(next)
                    self.visited.append(next)
                    # print(next)
        return False

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[id[1]])

    def passable(self, id):
        return self.maze[id[0]][id[1]] != self.wall

    def get_neighbours(self, id):
        (x,y) = id
        results = [(x+1,y),(x,y-1), (x-1,y), (x,y+1)]
        if (x + y) % 2 == 0: results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results



def path_finder(maze):
    lo = cl_maze(maze)
    return lo.exit_is_available()


if __name__ == '__main__':
    a = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])

    b = "\n".join([
        ".W.",
        ".W.",
        "W.."
    ])

    c = "\n".join([
        "......",
        "......",
        "......",
        "......",
        "......",
        "......"
    ])

    d = "\n".join([
        "......",
        "......",
        "......",
        "......",
        ".....W",
        "....W."
    ])

    print(path_finder(c))