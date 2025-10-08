class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Track both the current max and min, because negatives flip the sign
        curr_max = curr_min = res = nums[0]

        for num in nums[1:]:
            # If the num is negative, the signs of min and max get flipped and so we swap them to accomodate that
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            res = max(res, curr_max)    # Check if the new max is more than the previous ones

        return res