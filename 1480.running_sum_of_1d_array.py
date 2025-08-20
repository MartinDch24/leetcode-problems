#Resolved
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):   # Iterate from the 2nd to the last index
            nums[i] += nums[i-1]    # Calculate the prefix sum of each number by adding the previous element to the current one
        return nums

# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         acc = 0
#         res = [0] * n
#
#         for i in range(n):
#             acc += nums[i]
#             res[i] = acc
#
#         return res