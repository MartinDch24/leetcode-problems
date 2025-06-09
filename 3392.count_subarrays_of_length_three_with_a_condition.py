class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sub_arrs = 0
        for i in range(len(nums)-2):
            if 2*(nums[i]+nums[i+2])==nums[i+1]:
                sub_arrs+=1
        return sub_arrs