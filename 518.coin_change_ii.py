#Resolved
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] = <number of ways to make amount i with coins>
        dp = [0] * (amount+1)
        # Only 1 way to make an amount of 0
        dp[0] = 1

        for c in coins:
            # Skip negative indices by starting from c 
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
        
        return dp[amount]