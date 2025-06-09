class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        largest_i = max_difference = result = -float('Inf')

        n = len(nums)

        for k in range(2, n):
            largest_i = max(largest_i, nums[k-2])
            max_difference = max(max_difference, largest_i - nums[k-1])
            result = max(result, max_difference * nums[k])

        return result if result > 0 else 0