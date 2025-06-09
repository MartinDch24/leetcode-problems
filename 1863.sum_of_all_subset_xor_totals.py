class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for n in nums:
            ans = ans | n
        return ans * pow(2, len(nums)-1)

        # def dfs(i, xor):
        #     if i == len(nums):
        #         return xor
        #     take = dfs(i + 1, xor ^ nums[i])
        #     leave_out = dfs(i + 1, xor)
        #
        #     return take + leave_out
        #
        # return dfs(0, 0)
