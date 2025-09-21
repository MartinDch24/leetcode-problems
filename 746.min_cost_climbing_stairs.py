class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]

        dp = [0] * n    # min cost to reach step i
        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, n):
            # The cost of the current step to be reached, along with the cheaper way to reach the 1st or 2nd before it
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[n-1], dp[n-2])    # Either the first or the last step before the top