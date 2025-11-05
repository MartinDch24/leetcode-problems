#Resolved - 2
class Solution:
    def fib(self, n: int) -> int:
        # The Fibonacci sequence starts with 0 and 1, so we safe guard against those 2 edge cases
        if n <= 1:
            return n

        dp = [0] * (n+1)    # dp[i] = f(i)
        dp[1] = 1   # F(1) = 1

        for i in range(2, n+1):
            # Each new y is formed by adding up the previous 2
            # y = f(x) = f(x-1) + f(x-2)
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    # Iterative solution:
        # if n < 2:
        #     return n
        #
        # a, b = 0, 1
        # for _ in range(2, n + 1):  # Iterate through the values
        #     a, b = b, a + b
        #
        # return b

    # Memoization solution:
        # memo = {0: 0, 1: 1}  # Dictionary for memoization, so we avoid recomputing
        #
        # def helper(x):  # Recursive solution
        #     if x not in memo:  # Only compute if not cached
        #         memo[x] = helper(x - 1) + helper(x - 2)
        #     return memo[x]
        #
        # return helper(n)