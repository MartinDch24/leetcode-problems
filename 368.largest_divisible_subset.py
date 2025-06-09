class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()

        dp = {}

        for i in nums:
            longest_subset = []
            for j in dp:
                if i % j == 0 and len(dp[j]) > len(longest_subset):
                    longest_subset = dp[j]
            dp[i] = list(longest_subset) + [i]

        return max(dp.values(), key=len)
