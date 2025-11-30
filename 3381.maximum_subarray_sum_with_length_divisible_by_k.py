from math import inf


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref_sum = 0  # The sum up to the current num

        # If the length of a subarray is r-l+1 and we want it to be divisible by k
        # (r-l+1) % k == 0, then (r+1) % k == l % k
        # So we pair indices with the same mod together to get a valid subarray between them
        # mod_groups[m] = smallest pref_sum[j], were j%k == i%k == m
        mod_groups = [inf] * k
        mod_groups[-1] = 0  # prefix sum before the first element
        res = -inf  # Final sum

        for i, num in enumerate(nums):
            pref_sum += num
            m = i % k  # The mod of the current index

            # Compare the current res, to the new candidate
            # It is the total prefix sum so far - the smallest prefix sum of nums[j], were j%k == i%k
            res = max(res, pref_sum - mod_groups[m])

            # Update mod_groups with the new prefix sum at i, where m = i%k
            mod_groups[m] = min(mod_groups[m], pref_sum)

        return res