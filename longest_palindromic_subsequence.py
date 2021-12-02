def longest_palindromic_subsequence_rec(text):
    n = len(text)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if text[0] == text[n - 1]:
        return longest_palindromic_subsequence_rec(text[1:n - 1]) + 2
    return max(longest_palindromic_subsequence_rec(text[1:]), longest_palindromic_subsequence_rec(text[:n - 1]))


def longest_palindromic_subsequence_dp(text):
    n = len(text)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
        if i < n - 1 and text[i] == text[i + 1]:
            dp[i][i + 1] = 2
        elif i < n - 1 and text[i] != text[i + 1]:
            dp[i][i + 1] = 1
    j = 2
    while j < n:
        i = 0
        k = j
        while k < n:
            if text[i] == text[k]:
                dp[i][k] = dp[i + 1][k - 1] + 2
            else:
                dp[i][k] = max(dp[i + 1][k], dp[i][k - 1])
            k += 1
            i += 1
        j += 1
    return dp[0][n - 1]


if __name__ == "__main__":
    print(longest_palindromic_subsequence_rec("abbacababa"))
    print(longest_palindromic_subsequence_dp("abbacababa"))
