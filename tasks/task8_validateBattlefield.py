dct = {1:4, 2:3, 3:2, 4:1}
battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

maxLenShip = 4

def validateBattlefield(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                if diagonalChecks(i,j, field) == False:
                    return False
                if contactAnyOtherShipCheck(i,j, field) == False:
                    return False
    return True

def contactAnyOtherShipCheck(i,j, array):
    maxLenForShip(i,j, array)

def maxLenForShip(i,j, array):
    if i+4 < len(array):
        for x in range(i, i+4, 1):



def diagonalChecks(i,j,array):
    if ( rightLowDiagonalCheck(i,j,array) == False ) or \
            ( leftLowDiagonalCheck(i,j,array) == False ) or \
            ( rightUpDiagonalCheck(i,j,array) == False ) or \
            ( leftUpDiagonalCheck(i,j,array) == False ):
       return False


def rightLowDiagonalCheck(i,j,array):
    if i+1 != len(array):
        if j+1 != len(array[i]):
            if array[i+1][j+1] == 1:
                return False
    return True

def rightUpDiagonalCheck(i,j,array):
    if i != 0:
        if j+1 != len(array[i]):
            if array[i-1][j+1] == 1:
                return False
    return True

def leftLowDiagonalCheck(i,j,array):
    if i+1 != len(array):
        if j != 0:
            if array[i+1][j-1] == 1:
                return False
    return True

def leftUpDiagonalCheck(i,j,array):
    if i != 0:
        if j != 0:
            if array[i-1][j-1] == 1:
                return False
    return True




if __name__ == '__main__':
    validateBattlefield(battleField)

