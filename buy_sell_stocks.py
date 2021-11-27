from functools import lru_cache

# You are given an array of stock prices over the time.
# Calculate maximum profit of buy and sell stocks.
# You are not allowed to hold more than one stock at time.


def buy_sell_stocks_recursive(prices):
    @lru_cache(maxsize=None)
    def buy_sell_util(day, own_stock):
        if day < 0:
            if not own_stock:
                return 0
            else:
                return float("-inf")
        price = prices[day]

        if own_stock:
            buy = buy_sell_util(day - 1, False) - price
            hold = buy_sell_util(day - 1, True)
            return max(buy, hold)

        sell = buy_sell_util(day - 1, True) + prices[day]
        avoid = buy_sell_util(day - 1, False)

        return max(sell, avoid)

    return buy_sell_util(len(prices) - 1, False)


def buy_sell_stocks_dp(prices):
    prev_own = float('-inf')
    prev_not_own = 0
    n = len(prices)

    for i in range(n):
        buy = prev_not_own - prices[i]
        hold = prev_own
        own = max(buy, hold)

        sell = prev_own + prices[i]
        avoid = prev_not_own
        not_own = max(sell, avoid)
        prev_own = max(prev_own, own)
        prev_not_own = max(prev_not_own, not_own)

    return max(prev_not_own, prev_own)


def buy_sell_stocks_budget(prices, budget):
    prev_own = float('-inf')
    prev_not_own = budget
    n = len(prices)

    for i in range(n):
        buy = prev_not_own - prices[i]
        hold = prev_own
        prev_own = max(prev_own, buy, hold)
        if prev_own < 0:
            prev_own = float('-inf')

        sell = prev_own + prices[i]
        avoid = prev_not_own
        prev_not_own = max(prev_not_own, sell, avoid)

    return max(prev_own, prev_not_own)


def buy_sell_stocks_k_times(prices, k):
    n = len(prices)
    profit = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(1, k + 1):
            max_so_far = 0
            for l in range(i):
                max_so_far = max(max_so_far, prices[i] - prices[l] + profit[l][j - 1])
            profit[i][j] = max(profit[i - 1][j], max_so_far)
    return profit[n - 1][k]


if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(buy_sell_stocks_recursive(prices))
    print(buy_sell_stocks_dp(prices))
    print(buy_sell_stocks_budget(prices, 100))
    print(buy_sell_stocks_k_times(prices, 2))

