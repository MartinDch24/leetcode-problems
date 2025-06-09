class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_i = -float('Inf')
        largest_difference = -float('Inf')
        result = -float('Inf')

        for k in range(2, len(nums)):
            max_i = max(max_i, nums[k-2])
            largest_difference = max(largest_difference, max_i - nums[k-1])
            result = max(result, largest_difference * nums[k])

        return result if result > 0 else 0