def largest_square(matrix):
    largest = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                continue
            matrix[i][j] = 1 + min(matrix[i - 1][j],
                                   matrix[i][j - 1],
                                   matrix[i - 1][j - 1])
            if matrix[i][j] > largest:
                largest = matrix[i][j]
    return largest


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0, 1, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1],
    ]
    print(largest_square(matrix))
