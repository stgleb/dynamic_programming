def max_score_path(maze):
    n = len(maze)
    m = len(maze[0])

    reachable = True
    for i in range(1, n):
        if reachable and maze[i][0]:
            maze[i][0] += maze[i - 1][0]
        else:
            reachable = False
            maze[i][0] = 0

    reachable = True
    for j in range(1, m):
        if reachable and maze[0][j]:
            maze[0][j] += maze[0][j - 1]
        else:
            reachable = False
            maze[0][j] = 0

    for i in range(1, n):
        for j in range(1, m):
            if maze[i][j]:
                maze[i][j] = max(maze[i - 1][j], maze[i][j - 1])
    return maze[n - 1][m - 1]


if __name__ == "__main__":
    maze = [
        [2, 1, 9, 5, 8],
        [1, 0, 1, 7, 8],
        [3, 0, 2, 0, 0],
        [4, 5, 4, 3, 2],
    ]
    print(max_score_path(maze))
