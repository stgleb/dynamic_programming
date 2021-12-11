def largest_ractangle(heights):
    stack = []
    max_area = 0
    index = 0
    while index < len(heights):
        if (not stack) or (heights[stack[-1]] <= heights[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (heights[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))
            max_area = max(max_area, area)

    while stack:
        top_of_stack = stack.pop()
        area = (heights[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        max_area = max(max_area, area)
    return max_area


def largest_submatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    prefix = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 or matrix[i][j] == 0:
                prefix[i][j] = matrix[i][j]
            elif matrix[i][j]:
                prefix[i][j] = prefix[i - 1][j] + matrix[i][j]

    largest = 0
    for i in range(n):
        largest = max(largest, largest_ractangle(prefix[i]))
    return largest


if __name__ == "__main__":
    matrix = [
        [0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0],
    ]
    print(largest_submatrix(matrix))
