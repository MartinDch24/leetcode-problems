from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        freq_map = Counter(nums)    # {<num>: <times it appears>, ...}
        max_num = max(nums) # The largest number in the array

        earnings = [0] * (max_num + 1)  # DP array to find the max earnings for every i up to max_num

        for i in range(1, max_num + 1):
            # Either take the earnings of the previous number, i.e. don't delete nums[i]
            # Or delete nums[i] and so the max earnings become the max earnings of nums[i-2] + the points of the new number
            earnings[i] = max(
                earnings[i - 1],
                earnings[i - 2] + freq_map[i] * i
            )

        return earnings[max_num]

    # O(1) space solution:
    #
    # if not nums:
    #     return 0
    #
    # freq_map = Counter(nums)  # {<num>: <times it appears>, ...}
    # max_num = max(nums)  # The largest number in the array
    #
    # # The max points for i-2 nums and i-1 nums
    # prev2, prev1 = 0, 0
    #
    # for i in range(max_num + 1):
    #     # Either the max points for i-1 nums or the max points of i-2 nums + the points that deleting i would give
    #     curr = max(prev1, prev2 + freq_map.get(i, 0) * i)
    #
    #     # Move the window forward
    #     prev2 = prev1
    #     prev1 = curr
    #
    # return prev1  # prev1 is equal to curr at the end, but curr isn't initialized outside the loop