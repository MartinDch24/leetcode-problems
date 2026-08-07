class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]   # Max profit for holding the stock we've bought
        sold = float('-inf')    # Max profit from selling today
        rest = 0    # Max profit from not holding a stock and not in cooldown

        for p in prices[1:]:
            # Save the previous values of the variables to form the new ones
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            # Either continue holding or buy today after having rested
            hold = max(prev_hold, prev_rest - p)
            # Sell today
            sold = prev_hold + p
            # Either continue resting or finish yesterday's cooldown
            rest = max(prev_rest, prev_sold)

        # The max profit is either from the rests or selling
        return max(sold, rest)

        #DP Solution:

        # n = len(prices)
        # # 0: able to buy, 1: holding stock, 2: cooldown
        # dp = [[0] * 3 for _ in range(n)]

        # dp[0][0] = 0              # haven't bought anything
        # dp[0][1] = -prices[0]     # bought stock
        # dp[0][2] = float("-inf")  # cannot be on cooldown on the first day

        # for i in range(1, n):
        #     # You can be able to buy if you either didn't buy yesterday or you were on cooldown yesterday
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][2])
        #     # You are holding a stock if you were already holding it yesterday or you bought it yesterday
        #     dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        #     # To be on cooldown, you need to have sold your stock
        #     dp[i][2] = dp[i-1][1] + prices[i]

        # # You either end being able to buy or on cooldown, because holding is unrealized value
        # return max(dp[n-1][0], dp[n-1][2])