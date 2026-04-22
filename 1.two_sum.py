#Resolved
class Solution(object):
    def twoSum(self, nums, target):
        num_idx = {}  # Save the index of numbers we've gone over

        for i, num in enumerate(nums):
            goal = target - num # Since num + goal = target
            if goal in num_idx:
                return [i, num_idx[goal]]
            num_idx[num] = i