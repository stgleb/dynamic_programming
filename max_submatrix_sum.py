def max_subarray(a):
    total = 0
    n = len(a)
    max_sum = float('-inf')
    for i in range(n):
        total += a[i]
        if total < 0:
            total = 0
        if total > max_sum:
            max_sum = total
    return max_sum


def max_submatrix_sum(matrix):
    prefix = [row[:] for row in matrix]

    n = len(prefix)
    m = len(prefix[0])
    for i in range(n):
        for j in range(m):
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]

    s = float('-inf')
    for i in range(n):
        for k in range(i):
            row = prefix[i][:]
            for j in range(m):
                row[j] -= prefix[k][j]
            tmp = max_subarray(row)
            if tmp > s:
                s = tmp
        tmp = max_subarray(prefix[i][:])
        if tmp > s:
            s = tmp
    return s


if __name__ == "__main__":
    matrix = [ [ 0, -2, -7, 0 ],
               [ 9, 2, -6, 2 ],
               [ -4, 1, -4, 1 ],
               [ -1, 8, 0, -2 ] ]
    print(max_submatrix_sum(matrix))

