def longest_valid_parenthesis(s):
    stack = [-1]
    start, end = 0, 0
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()

            if len(stack) > 0:
                if i - stack[-1] > max_len:
                    max_len = i - stack[-1]
                    start = stack[-1]
                    end = i
            else:
                stack.append(i)

    return max_len, s[start + 1:end + 1]


if __name__ == "__main__":
    print(longest_valid_parenthesis("()(())()))()()()()()()()"))
