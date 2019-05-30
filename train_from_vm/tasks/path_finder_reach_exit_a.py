
class cl_maze:
    def __init__(self, maze):
        self.maze = maze.split('\n')
        self.wave_front = []
        self.start = (0, 0)
        self.finish = (len(self.maze) - 1, len(self.maze[len(self.maze) - 1]) - 1)
        self.exit = False
        self.wall = 'W'
        self.weights = {}

    def exit_is_available(self):
        self.wave_front.append(self.start)
        cost_so_far = {}
        cost_so_far[self.start] = 0

        while len(self.wave_front) != 0:
            current = self.wave_front[0]
            self.wave_front.remove(current)
            if current == self.finish: return True

            for next in self.get_neighbours(current):
                new_cost = cost_so_far[current] + self.cost(next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    self.wave_front.append(next)
        return False

    def cost(self, node):
        return self.weights.get(node,1)

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[id[1]])

    def passable(self, id):
        return self.maze[id[0]][id[1]] != self.wall

    def get_neighbours(self, id):
        (x,y) = id
        results = [(x+1,y),(x,y-1), (x-1,y), (x,y+1)]
        # if (x + y) % 2 == 0: results.reverse()
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

    print(path_finder(a))