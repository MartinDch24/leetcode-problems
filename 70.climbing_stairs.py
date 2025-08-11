class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:  # The base cases 0, 1 and 2
            return n

        dp = [0] * (n + 1)  # A table where dp[i] = number of ways to reach step i
        dp[1], dp[2] = 1, 2  # Put in the values of the base cases

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[
                i - 2]  # The number of ways to reach step n is the ways to reach step n-1 and the ways to reach step n-2 summed together

        return dp[n]