def check_interleave_rec(text, s1, s2):
    if not text and not s1 and not s2:
        return True

    if not text and (s1 or s2):
        return False

    if s1 and s2 and text[0] == s1[0] and text[0] == s2[0]:
        return check_interleave_rec(text[1:], s1[1:], s2) or \
               check_interleave_rec(text[1:], s1, s2[1:])
    if s1 and text[0] == s1[0]:
        return check_interleave_rec(text[1:], s1[1:], s2)
    if s2 and text[0] == s2[0]:
        return check_interleave_rec(text[1:], s1, s2[1:])
    return False


def check_interleave_dp(text, s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0:
                if text[j - 1] == s2[j - 1]:
                    dp[i][j] = dp[i][j - 1]
            elif j == 0:
                if text[i - 1] == s1[i - 1]:
                    dp[i][j] = dp[i - 1][j]
            elif text[i + j - 1] == s1[i - 1] and text[i + j - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j]
            elif text[i + j - 1] == s2[j - 1] and text[i + j - 1] != s1[i - 1]:
                dp[i][j] = dp[i][j - 1]
            elif text[i + j - 1] == s2[j - 1] and text[i + j - 1] == s1[i - 1]:
                dp[i][j] = (dp[i][j - 1] or dp[i - 1][j])
    return dp[n][m]


if __name__ == "__main__":
    print(check_interleave_rec("XXY", "XX", "Y"))
    print(check_interleave_rec("XYXXY", "XXX", "YY"))

    print(check_interleave_dp("XXY", "XX", "Y"))
    print(check_interleave_dp("XYXXY", "XXX", "YY"))
