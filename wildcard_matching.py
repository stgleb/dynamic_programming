def is_match_rec(text, pattern):
    if not text and not pattern:
        return True
    elif not text or not pattern:
        return False
    elif pattern[0] == "?":
        return is_match_rec(text[1:], pattern[1:])
    elif pattern[0] == "*":
        return is_match_rec(text[1:], pattern) or is_match_rec(text[1:], pattern[1:])
    elif pattern[0] == text[0]:
        return is_match_rec(text[1:], pattern[1:])
    return False


def is_match_dp(text, pattern):
    n = len(text)
    m = len(pattern)
    if m == 0:
        return n == 0
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    for j in range(1, m + 1):
        if pattern[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 0:
                dp[i][j] = False
            elif pattern[j - 1] == "*":
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif pattern[j - 1] == text[i - 1] or pattern[j - 1] == "?":
                dp[i][j] = dp[i - 1][j - 1]
    return dp[n][m]


if __name__ == "__main__":
    text = "baaabab"
    print(is_match_rec(text, "ba***ab"))
    print(is_match_rec(text, "baaa?ab"))
    print(is_match_rec(text, "ba*a?"))
    print(is_match_rec(text, "a*ab"))
    print("-----------------------")
    print(is_match_dp(text, "ba***ab"))
    print(is_match_dp(text, "baaa?ab"))
    print(is_match_dp(text, "ba*a?"))
    print(is_match_dp(text, "a*ab"))
