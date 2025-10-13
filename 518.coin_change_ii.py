class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)   # Combinations for each amount from 0 to amount
        dp[0] = 1   # We have 1 combination to achieve 0 and it's no coins

        for c in coins: # Iterate over the coins first to get only unique combinations
            for i in range(c, amount+1):
                # Start from the given coin, so index remains non-negative
                dp[i] += dp[i-c]    # Add combinations to get amount i-c to the combinations to get amount i

        return dp[amount]