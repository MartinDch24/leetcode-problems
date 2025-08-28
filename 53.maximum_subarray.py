class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = 0  # The sum we have so far
        max_sum = nums[0]  # The largest sum so far

        for i in range(len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[
                i])  # We either end the subarray and start a new one at nums[i] or extend the current subarray, depending on which value is greater
            max_sum = max(max_sum, curr_sum)  # Check if our current sum is greater than the maximum sum

        return max_sum