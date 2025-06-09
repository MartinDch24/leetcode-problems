class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        acc = 0
        res = [0] * n

        for i in range(n):
            acc += nums[i]
            res[i] = acc

        return res