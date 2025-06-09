class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sub_arrs = 0
        left = 0
        arr_sum = 0
        for right in range(len(nums)):
            arr_sum += nums[right]

            while arr_sum * (right - left + 1) >= k and left <= right:
                arr_sum -= nums[left]
                left += 1

            sub_arrs += right - left + 1
        return sub_arrs
