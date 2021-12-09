def pick_up_rec(coins):
    def util(coins, turn):
        if len(coins) == 0:
            return 0
        if len(coins) == 1:
            return coins[0]
        if len(coins) == 2:
            return max(coins)
        if turn:
            return max(util(coins[1:], False) + coins[0], coins[-1] + util(coins[:len(coins) - 1], False))
        return min(util(coins[1:], True), util(coins[:len(coins) - 1], True))

    return util(coins, True)


def pick_up_dp(coins):
    n = len(coins)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = coins[i]
        if i < n - 1:
            dp[i][i + 1] = max(coins[i], coins[i + 1])

    j = 2
    turn = True
    while j < n:
        i = 0
        k = j
        turn = not turn
        while k < n:
            if turn:
                dp[i][k] = max(dp[i + 1][k] + coins[i], dp[i][k - 1] + coins[k])
            else:
                dp[i][k] = min(dp[i + 1][k], dp[i][k - 1])
            i += 1
            k += 1
        j += 1
    return dp[0][n - 1]


if __name__ == "__main__":
    coins = [2, 7, 1, 5, 6, 3]
    print(pick_up_rec(coins))
    print(pick_up_dp(coins))
