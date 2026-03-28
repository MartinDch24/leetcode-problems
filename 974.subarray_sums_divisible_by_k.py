from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        # (nums[i] - nums[j]) % k == 0 => nums[i] % k == nums[j] % k
        # We are saving how many prefix sums have the same mod of k
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            mod = curr_sum % k

            # We are looking to add every possible pair of same-mod subarrays as a count to res
            res += prefix_count[mod]
            prefix_count[mod] += 1

        return res