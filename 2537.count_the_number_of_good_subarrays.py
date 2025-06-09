class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sub_arrs = 0
        pairs = {}
        pair_count = 0
        left = 0

        n = len(nums)

        for right in range(n):
            if nums[right] in pairs:
                pair_count += pairs[nums[right]]
                pairs[nums[right]] += 1
            else:
                pairs[nums[right]] = 1

            while pair_count >= k:
                sub_arrs += n - right
                pairs[nums[left]] -= 1
                pair_count -= pairs[nums[left]]
                left += 1

        return sub_arrs