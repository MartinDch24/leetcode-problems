#Resolved - 3
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] = <max amount of coins that can be collected strictly between i and j, leaving balloons nums[i] and nums[j] intact>
        dp = [[0] * n for _ in range(n)]

        # Iterate over the smaller intervals first
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                # If nums[k] is the last popped balloon in the interval [i+1:j],try every k
                dp[i][j] = max(dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j] for k in range(i+1, j))

        return dp[0][n-1]