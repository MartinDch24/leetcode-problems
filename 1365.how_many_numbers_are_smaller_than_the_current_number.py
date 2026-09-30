class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        freq_map = Counter(nums)    # get the amounts of each number in the nums array
        # Since nums can only be from 1 to 100, we can save how many numbers are smaller than i with prefix sums
        less_than = [0] * 101 # less_than[num] = <amount of numbers less than num>

        for num in range(1, 101):
            # We know that all the nums that are less than num-1 are also less than num,
            # So we sum them up with the amount of numbers that are equal to num-1
            less_than[num] += freq_map[num-1] + less_than[num-1]

        return [less_than[num] for num in nums]