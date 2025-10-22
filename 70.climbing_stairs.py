#Resolved
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:  # Edge cases
            return n

        dp = [1] * (n+1)    # dp[i] = ways to climb i stairs

        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]   # Climb up to step i from either step i-1 or step i-2

        return dp[n]