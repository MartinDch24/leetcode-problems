#Resolved - 3
class Solution:
    def rob(self, nums: List[int]) -> int:
        # We have n number of houses
        if len(nums) == 1:  # If there's only one house, just rob it
            return nums[0]

        # prev2 = max money if we stop 2 houses back
        # prev1 = max money if we stop at the previous house
        prev2, prev1 = 0, 0

        for num in nums:
            curr = max(prev2+num, prev1)    # The number of houses so far. We use max() to check whether we'd get more money by robbing the current house and the one 2 before it (not adjacent) or by skipping it and settling for robbing the previous house
            prev2, prev1 = prev1, curr  # Move the window forward

        return prev1 # The max amount of money for n houses b
    
        #DP array solution:
        # n = len(nums)
        # if n == 1:
        #     return nums[0]

        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        # Either take the value of the adjacent house or skip it, take the one 2 houses back and add the value of the current one
        #     dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        # return max(dp[n-1], dp[n-2])