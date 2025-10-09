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