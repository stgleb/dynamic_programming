import copy


def submatrix_sum(matrix, top, left, bottom, right):
    prefix = copy.copy(matrix)
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if i != 0:
                prefix[i][j] += prefix[i - 1][j]
            if j != 0:
                prefix[i][j] += prefix[i][j - 1]

    return prefix[top][right] - prefix[top][left] - prefix[bottom][right] + prefix[bottom][left]


if __name__ == "__main__":
    matrix = [
        [2, 3, -4, 5, 2],
        [1, 1,  2, 5, 7],
        [2, 4, 1, 7,  0],
        [6, 5, 1, -4, 9],
        [0, 1, -1, 0, 0],
    ]
    print(submatrix_sum(matrix, 3, 1, 1, 4))
