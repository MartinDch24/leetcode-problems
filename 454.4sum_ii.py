from collections import defaultdict


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        a_b_sums = defaultdict(int) # {<sum1>: <how many ways it can be acheived>, <sum2>: ...}
        result = 0  # Number of tuples

        for n1 in nums1:
            for n2 in nums2:
                a_b_sums[n1+n2] += 1  # Save how many times each sum appears

        # For a sum of 4 numbers to equal 0
        # That means that the sum of the 3rd and 4th number is the negative value of the sum of the 1st and 2nd number
        for n3 in nums3:
            for n4 in nums4:
                # Since we use defaultdict, if the sum isn't in the precomputed ones, it will just add 0
                # Otherwise it will add the number of times the sum appears as a combination from nums1 and nums2
                # We add the count, since that is also all the ways we can make a valid tuple
                result += a_b_sums[-(n3+n4)]

        return result