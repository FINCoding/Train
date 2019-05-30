def nb_find(n, pos, maze):  # find "." neighbours of a position
    nb_loc = set()
    try:  # check East and South, may be out of string range
        if maze[pos + 1] == ".":
            nb_loc.add(pos + 1)
        if maze[pos + n + 1] == ".":
            nb_loc.add(pos + n + 1)
    except:
        None
    if pos > 1 and maze[pos - 1] == ".":  # check West
        nb_loc.add(pos - 1)
    if pos > n + 1 and maze[pos - n - 1] == ".":  # check North
        nb_loc.add(pos - n - 1)

    return (nb_loc)


import math


def path_finder(maze):
    if maze == ".": return True  # handle extreme case
    n = int(math.sqrt(len(maze)))  # find number of rows
    all_loc = test_loc = {0}
    for e in range(len(maze)):
        nb_loc = set()
        for i in test_loc:
            nb_loc = nb_loc.union(nb_find(n, i, maze))  # find neighbours of every test_loc
        if all_loc.union(nb_loc) == all_loc:  # check if no new neighbours found
            break

        test_loc = nb_loc.difference(all_loc)  # test only new neighbours found
        all_loc = all_loc.union(test_loc, nb_loc)  # update all_loc
        if len(maze) - 1 in all_loc: return True

    return False  # can go to lower right corner from upper left one