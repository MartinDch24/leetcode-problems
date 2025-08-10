class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * (n + 1)  # A table to save all values, where dp[i] = F(i)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]  # Fill in the table

        return dp[n]

    #Iterative solution:
        # if n < 2:
        #     return n
        #
        # a, b = 0, 1
        # for _ in range(2, n + 1):  # Iterate through the values
        #     a, b = b, a + b
        #
        # return b