class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        last_minK = last_maxK = last_invalid = -1
        sub_arrs = 0

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            if nums[i] == minK:
                last_minK = i
            if nums[i] == maxK:
                last_maxK = i

            smallest_idx = min(last_minK, last_maxK)
            if smallest_idx > -1 and smallest_idx > last_invalid:
                sub_arrs += smallest_idx - last_invalid

        return sub_arrs

