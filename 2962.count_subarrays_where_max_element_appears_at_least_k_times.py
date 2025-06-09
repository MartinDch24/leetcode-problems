class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        sub_arrs = 0
        max_el = max(nums)
        max_count = 0
        left = 0

        for right in range(n):
            if nums[right] == max_el:
                max_count += 1

            while max_count >= k:
                sub_arrs += n - right
                if nums[left] == max_el:
                    max_count -= 1
                left += 1

        return sub_arrs