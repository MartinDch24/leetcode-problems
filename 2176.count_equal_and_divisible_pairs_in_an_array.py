class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pairs = {}
        pair_count = 0

        for j in range(n):
            if nums[j] in pairs:
                for i in pairs[nums[j]]:
                    if j * i % k == 0:
                        pair_count += 1
                pairs[nums[j]].add(j)
            else:
                pairs[nums[j]] = {j}

        return pair_count