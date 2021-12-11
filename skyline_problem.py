def max_rectangle_n2(heights):
    max_square = 0
    n = len(heights)

    for i in range(n):
        min_height = float('inf')
        for j in reversed(range(i)):
            if heights[j] < min_height:
                min_height = heights[j]
            square = min_height * (i - j)
            max_square = max(square, max_square)
    return max_square


def skyline(heights):
    n = len(heights)
    stack = []
    max_square = 0

    for i in range(n):
        h = heights[i]
        while stack and heights[stack[-1]] >= h:
            square = (i - stack[-1]) * heights[stack[-1]]
            max_square = max(square, max_square)
            stack.pop()
        if len(stack) == 0:
            square = (i + 1) * h
            max_square = max(square, max_square)
        stack.append(i)
    while stack:
        square = (len(heights) - stack[-1]) * heights[stack[-1]]
        max_square = max(square, max_square)
        stack.pop()

    return max_square


if __name__ == "__main__":
    heights = [2, 5, 7, 1, 3, 8, 9, 4]
    print(max_rectangle_n2(heights))
    print(skyline(heights))
