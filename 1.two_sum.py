#Resolved - 2
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        processed = {}  # Save the nums we've gone over with their index
        for i, num in enumerate(nums):
            # Check if we've already found a number, where number + nums[i] = target
            # number = target - num
            if target - num in processed:
                return [processed[target-num], i]
            processed[num] = i