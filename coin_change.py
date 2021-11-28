from collections import deque


# Given a set of coin values and amount to give
# figure out optimal set of coins to make this amount.


def coin_change_rec(coins, amount):
    if amount == 0:
        return []
    if amount < 0:
        return None
    if len(coins) == 0:
        return None
    n = len(coins)
    result = None
    take_coin_result = coin_change_rec(coins, amount - coins[n - 1])
    if take_coin_result is not None:
        result = take_coin_result + [coins[n - 1]]
    not_take_coin_result = coin_change_rec(coins[:n - 1], amount)
    if result is None or (not_take_coin_result is not None and len(not_take_coin_result) < len(result)):
        result = not_take_coin_result
    return result


def coin_change_bfs(coins, amount):
    queue = deque([(amount, coins, [])])
    result = None
    while queue:
        amount, coins, split = queue.popleft()
        if amount == 0 and (result is None or len(split) < len(result)):
            result = split
        if amount < 0:
            continue
        if not coins:
            continue
        n = len(coins)
        queue.append((amount - coins[n - 1], coins, split + [coins[n - 1]]))
        queue.append((amount, coins[:n - 1], split))
    return result


def coin_change_dp(coins, amount):
    dp = [[float('inf') for _ in range(len(coins))] for _ in range(amount + 1)]
    for j in range(len(coins)):
        dp[0][j] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] > i:
                break
            if dp[i][j] > dp[i - coins[j]][j] + 1:
                dp[i][j] = dp[i - coins[j]][j] + 1
            if dp[i][j] > dp[i][j - 1]:
                dp[i][j] = dp[i][j - 1]
    i = amount
    j = len(coins) - 1
    result = []
    while i >= 0 and j >= 0:
        if i == 0:
            break
        if j == 0 and i > 0:
            result = None
            break
        if i >= coins[j] and dp[i][j] != float('inf') and dp[i][j] <= dp[i][j - 1]:
            result = result + [coins[j]]
            i -= coins[j]
        else:
            j -= 1
    return result


def coin_change_count_ways_rec(coins, amount):
    if amount == 0:
        return 1
    if amount < 0 or len(coins) == 0:
        return 0
    n = len(coins)
    return coin_change_count_ways_rec(coins, amount - coins[-1]) \
           + coin_change_count_ways_rec(coins[:n - 1], amount)


def coin_change_count_ways_dp(coins, amount):
    n = len(coins)
    dp = [[0 for _ in range(n)] for _ in range(amount + 1)]
    for i in range(n):
        dp[0][i] = 1

    for i in range(1, amount + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i][j] += dp[i - coins[j]][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    return dp[amount][n - 1]


if __name__ == "__main__":
    coins = (1, 2, 5)
    amount = 17
    print(coin_change_rec(coins, amount))
    print(coin_change_bfs(coins, amount))
    print(coin_change_dp(coins, amount))
    print(coin_change_count_ways_rec(coins, amount))
    print(coin_change_count_ways_dp(coins, amount))
