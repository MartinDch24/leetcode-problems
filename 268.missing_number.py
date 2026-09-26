class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        goal_sum = sum(i for i in range(n+1))
        curr_sum = sum(nums)

        # Since nums contains all numbers in the range [0; n], except one, subtracting the sum of nums from the sum of the range [0; n] will leave us with the missing number
        return goal_sum - curr_sum