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


if __name__ == "__main__":
    heights = [2, 5, 7, 1, 3, 8, 9, 4]
    print(max_rectangle_n2(heights))
    print(skyline(heights))
    print(max_rectangle_n2([1, 0, 5, 3, 5, 1]))
    print(skyline([1, 0, 5, 3, 5, 1]))
