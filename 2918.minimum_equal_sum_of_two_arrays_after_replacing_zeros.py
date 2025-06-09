class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        s1 = sum(nums1)
        s2 = sum(nums2)

        min1 = s1 + z1
        min2 = s2 + z2

        target = max(min1, min2)

        if z1 == 0 and s1 != target: return -1
        if z2 == 0 and s2 != target: return -1

        return target