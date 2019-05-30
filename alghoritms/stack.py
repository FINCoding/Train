class Stack:
    def __init__(self, n):
        self.N = n
        t = [0 for i in range(self.N)]
        print(t)
    def empty(self):
        global N
        return self.N == 0


if __name__ == '__main__':
    s = Stack(10)
    print(s.empty())
