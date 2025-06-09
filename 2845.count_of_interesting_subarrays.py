from collections import defaultdict
class Solution(object):
    def countInterestingSubarrays(self, nums, modulo, k):
        """
        :type nums: List[int]
        :type modulo: int
        :type k: int
        :rtype: int
        """
        prefix_count = 0
        sub_arrs = 0
        count_map = defaultdict(int)
        count_map[0] = 1

        for num in nums:
            if num % modulo == k:
                prefix_count += 1

            needed_prefix = (prefix_count - k) % modulo

            sub_arrs += count_map[needed_prefix]

            count_map[prefix_count % modulo] += 1

        return sub_arrs

        # n = len(nums)
        #
        # bi_vals = [1 if num % modulo == k else 0 for num in nums]
        # prefix_sums = 0
        # sub_arrs = 0
        # freq_map = defaultdict(int)
        # freq_map[0] = 1
        #
        # for right in range(n):
        #     prefix_sums += bi_vals[right]
        #     target = (prefix_sums - k) % modulo
        #     if target in freq_map:
        #         sub_arrs += freq_map[target]
        #
        #     remainder = prefix_sums % modulo
        #     freq_map[remainder] += 1
        #
        # return sub_arrs