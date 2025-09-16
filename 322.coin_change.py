class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float("inf")] * (amount+1)  # min_coins[<amount1>] = <min coins to get that amount> and so on...
        min_coins[0] = 0    # We start with 0 coins for amount 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    # If i-c < 0, we can't get it with any coins

                    # 1 new coin + the smallest number of coins to get the value of (i - the value of the new coin)
                    # If we can't get the amount of i-c with any coins, then min_coins[i] will just remain float("inf")
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i-c])

        # If we couldn't find a viable way to build to amount, then min_val remains float("inf") and min_coins[amount] has a value of float("inf")
        return -1 if min_coins[amount] == float("inf") else min_coins[amount]