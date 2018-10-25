class Point:
    def __init__(self, row, col):
        self.row = row
        self.col = col

def GetPacManResult(N, M, point):
    if point.row < 0 or point.row > N or point.col < 0 or point.col > M:
        raise Exception("wrong input data")

    start = 0
    end = M - 1
    direction = 1
    pointsCount = 1

    for i in range(1,N+1):
        for j in range(start, end + direction, direction):
            if (i == point.row  and j == point.col - 1):
                return pointsCount
            pointsCount += 1
        direction *= -1

        start, end = end, start
    return pointsCount

if __name__ == '__main__':
    print(GetPacManResult(3,3,Point(1,3)))





