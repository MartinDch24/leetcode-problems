#Resolved
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] = (<min product ending at i>, <max product ending at i>)
        dp = [[nums[0], nums[0]] for _ in range(n)]
        res = nums[0]

        for i in range(1, n):
            prev_min, prev_max = dp[i - 1]

            if nums[i] < 0:
                prev_min, prev_max = prev_max, prev_min

            # Either continue the subarray or start a new one
            curr_min = min(prev_min * nums[i], nums[i])
            curr_max = max(prev_max * nums[i], nums[i])

            dp[i] = (curr_min, curr_max)
            res = max(res, curr_max)

        return res