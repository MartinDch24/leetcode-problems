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

        #Kadane's algorithm:

        # curr_sum = 0  # The largest sum ending at the current number
        # max_sum = nums[0]  # The largest sum
        #
        # for num in nums:
        #     # Either the current sum + the new number or just the new number
        #     curr_sum = max(curr_sum + num, num)
        #
        #     # Check if the current sum is larger than the max_sum so far
        #     max_sum = max(curr_sum, max_sum)
        #
        # return max_sum