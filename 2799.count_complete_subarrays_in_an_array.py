class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_unique = len(set(nums))
        freq_map = {}
        left = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] in freq_map:
                freq_map[nums[right]] += 1
            else:
                freq_map[nums[right]] = 1

            while len(freq_map) == total_unique:
                res += len(nums) - right

                freq_map[nums[left]] -= 1
                if freq_map[nums[left]] == 0:
                    del freq_map[nums[left]]

                left += 1

        return res
    
#         total_unique_nums = len(set(nums))
#         nums_len = len(nums)
#
#         def at_most_k_unique_values(k):
#             left = 0
#             nums_freq_map = {}
#             valid_sub_arrs = 0
#
#             for right in range(nums_len):
#                 if nums[right] in nums_freq_map:
#                     nums_freq_map[nums[right]] += 1
#                 else:
#                     nums_freq_map[nums[right]] = 1
#
#                 while len(nums_freq_map) > k:
#                     nums_freq_map[nums[left]] -= 1
#                     if nums_freq_map[nums[left]] == 0:
#                         del nums_freq_map[nums[left]]
#
#                     left += 1
#
#                 valid_sub_arrs += right-left+1
#
#             return valid_sub_arrs
#
#         return at_most_k_unique_values(total_unique_nums) - at_most_k_unique_values(total_unique_nums-1)