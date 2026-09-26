class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # O(1) Space solution:
        res = []
        for i in range(len(nums)):
            # Use the values of nums as indexes
            index = abs(nums[i]) - 1

            # Mark the position of each index, by making the value there negative, so you don't corrupt the value and can use it with abs()
            nums[index] = -abs(nums[index])

        for i in range(len(nums)):
            # The index of each non-negative number in nums is a number that wasn't in nums
            if nums[i] > 0:
                res.append(i + 1)

        return res