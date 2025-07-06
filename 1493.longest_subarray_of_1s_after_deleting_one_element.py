class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        zeros_in_window = 0

        left = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_in_window += 1

            while zeros_in_window > 1:   # We want to have a window of 1s, with only one 0 in it
                if nums[left] == 0:
                    zeros_in_window -= 1
                left += 1   # We shrink the window from the left, until that is achieved

            max_len = max(max_len, right-left)  # We compare the current window's length to the others and take the max

        return max_len