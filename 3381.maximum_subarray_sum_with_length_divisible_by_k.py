from collections import defaultdict


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref_sum = [0] * (n + 1)  # pref_sum[i] = sum(nums[0..i-1])

        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + nums[i]

        # If the length of a subarray is r-l+1 and we want it to be divisible by k
        # (r-l+1) % k == 0, then (r+1) % k == l % k
        # So we pair indices with the same mod together to get a valid subarray between them
        # mod_groups[m] = smallest pref_sum[j], were j%k == i%k == m
        mod_groups = defaultdict(lambda: float('inf'))
        res = -float("inf")  # Final sum

        for i in range(n + 1):
            m = i % k  # The mod of the current index

            # If we already have computed for the same modulo before
            # The new result candidate is pref_sum[i] - pref_sum[j], were j%k = i%k and pref_sum[j] is as small as possible
            if m in mod_groups:
                res = max(res, pref_sum[i] - mod_groups[m])

            # Update mod_groups with the new prefix sum at i, where m = i%k
            mod_groups[m] = min(mod_groups[m], pref_sum[i])

        return res