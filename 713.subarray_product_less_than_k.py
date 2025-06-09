class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        sub_arrs = 0
        n = len(nums)
        prod = 1

        for r in range(n):
            prod *= nums[r]
            while prod >= k and l<=r:
                prod = prod // nums[l]
                l+=1
            sub_arrs += r-l+1

        return sub_arrs
