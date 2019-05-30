import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

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
        frontier = Queue()
        frontier.put(self.start)
        self.visited.append(self.start)

        while not frontier.empty():
            current = frontier.get()

            for next in self.get_neighbours(current):
                if next not in self.visited:
                    frontier.put(next)
                    self.visited.append(next)
                    print(next)

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < len(self.maze[id[0]]) and 0 <= y < len(self.maze)

    def passable(self, id):
        return self.maze[id[0]][id[1]] != self.wall

    def get_neighbours(self, id):
        (x,y) = id
        results = [(x+1,y),(x,y-1), (x-1,y), (x,y+1)]
        print(results)
        if (x + y) % 2 == 0: results.reverse()
        print('reverse results %s' % results)
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

    path_finder(a)