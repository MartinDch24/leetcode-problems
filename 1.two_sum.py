class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_pairs = {}

        for i, num in enumerate(nums):
            goal_num = target - num
            if goal_num in num_pairs:
                return [num_pairs[goal_num], i]

            num_pairs[num] = i