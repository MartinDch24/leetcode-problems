class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 0: not holding, transaction 1
        # 1: holding, transaction 1
        # 2: not holding, transaction 2
        # 3: holding, transaction 2
        # 4: not holding, after completing transaction 2
        dp = [[0] * 5 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        # You couldn't have completed the first transaction on day 1
        dp[0][2] = float("-inf")
        dp[0][3] = float("-inf")

        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        # The max profit from either 0, 1 or 2 transactions
        return max(dp[n-1][0], dp[n-1][2], dp[n-1][4])