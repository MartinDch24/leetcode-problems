class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n    # Array to store the max money for i+1 houses
        dp[0] = nums[0] # We have only 1 house, so the most money we can get will be by robbing it
        dp[1] = max(nums[0], nums[1])   # We have only 2 houses and since they'll be adjacent, we rob the one with more money

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # For house i, we have the choice of skipping it (thus max money being dp[i-1]) or robbing it (which will mean forfeiting the previous house, since it's adjacent and robbing the house i-2 (the one left of i-1), making max money dp[i-2] + whatever money house i has)

        return dp[-1]   # After building dp for every i, we return the max amount of money for n houses, where n is the length of the inputet array