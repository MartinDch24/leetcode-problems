class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n  = len(prices)
        # 0: Transaction 1 - not holding
        # 1: Transaction 1 - holding
        # 2: Transaction 2 - not holding
        #              ...
        # 2*k-1: Transaction k - holding
        # 2*k: not holding - after completing transaction k
        dp = [[0] * (k*2 +1) for _ in range(n)]
        
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # Couldn't have completed transaction 1 on the first day
        for i in range(2, 2*k+1):
            dp[0][i] = float('-inf')

        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            for j in range(1, 2*k+1, 2):
                # Currently holding
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
                # Currently not holding (completed last transaction if j == k*2)
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] + prices[i])
        
        # Only consider the not-holding states, because if you are holding, then that's unrealized profit
        return max(dp[n-1][j] for j in range(0, 2*k+1, 2))