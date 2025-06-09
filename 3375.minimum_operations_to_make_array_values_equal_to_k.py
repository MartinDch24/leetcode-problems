class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        unique_nums = set(nums)

        smallest_num = min(unique_nums)

        if smallest_num < k:
            return -1
        elif smallest_num > k:
            return len(unique_nums)
        else:
            return len(unique_nums) - 1