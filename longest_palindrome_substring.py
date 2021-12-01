def longest_palindrome_substring_rec(s):
    def util(s):
        if not s:
            return True, 0
        if len(s) == 1:
            return True, 1
        if len(s) == 2 and s[0] != s[-1]:
            return False, 0
        if s[0] == s[-1]:
            is_palindrome, pal_len = util(s[1:len(s) - 1])
            if is_palindrome:
                return True, pal_len + 2

        is_pal1, len1 = util(s[1:])
        is_pal2, len2 = util(s[:len(s) - 1])
        return False, max(len1, len2)

    return util(s)[1]


def longest_palindrome_substring_dp(s):
    n = len(s)
    dp = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True

    j = 2
    max_len = 0
    start, end = 0, 0
    while j < n:
        i = 0
        k = j
        while k < n:
            if s[i] == s[k] and dp[i + 1][k - 1]:
                dp[i][k] = True
                if max_len < k - i + 1:
                    start = i
                    end = k
                    max_len = max(max_len, k - i + 1)
            k += 1
            i += 1
        j += 1
    return max_len, s[start:end + 1]


if __name__ == "__main__":
    print(longest_palindrome_substring_rec("atbtbatt"))
    print(longest_palindrome_substring_dp("atbtbatt"))

