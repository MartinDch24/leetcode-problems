class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # We can either skip the last house or skip the first, before starting to rob the housese, since they're adjacent
        prev1_first, prev2_first = 0, 0

        for n in nums[:-1]: # Skip last house
            # Either the previous house's money, or the money of the one before it with the money of the current one
            curr = max(prev1_first, prev2_first + n)
            prev2_first = prev1_first
            prev1_first = curr

        prev1_second, prev2_second = 0, 0
        for n in nums[1:]:  # Skip the first house
            curr = max(prev1_second, prev2_second + n)
            prev2_second = prev1_second
            prev1_second = curr

        # Since in the end, the highest amount of money for both approaches ends up being stored in curr and from there into prev1, we just compare the prev1 of both approaches and return the higher value
        return max(prev1_first, prev1_second)