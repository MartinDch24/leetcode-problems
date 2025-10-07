#Resolved
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #DP solution:

        n = len(nums)
        dp = [nums[0]] * n  # Max subarray ending at index i

        for i in range(1, n):
            # Either continue the previous subarray or start a new one
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)  # Return the largest sum of the calculated ones