def number_of_ways(maze):
    n = len(maze)
    m = len(maze[0])

    reachable = True
    for i in range(1, n):
        if maze[i - 1][0] != -1 and reachable:
            maze[i][0] = 1
        else:
            maze[i][0] = 0
            reachable = False

    reachable = True
    for j in range(1, m):
        if maze[0][j - 1] != -1 and reachable:
            maze[0][j] = 1
        else:
            reachable = False
            maze[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if maze[i][j] != -1:
                if maze[i][j - 1] != -1:
                    maze[i][j] += maze[i][j - 1]
                if maze[i - 1][j] != -1:
                    maze[i][j] += maze[i - 1][j]
    return maze[n - 1][m - 1]


if __name__ == "__main__":
    maze = [
        [0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0],
        [0, -1, 0, -1, -1],
        [0, 0, 0, 0, 0],
    ]
    print(number_of_ways(maze))
