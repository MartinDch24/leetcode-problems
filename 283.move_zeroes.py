#Resolved - 2
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0  # The position of the next non-zero

        for i in range(len(nums)):
            if nums[i] != 0:
                # We know that everything before nums[pos] is non-zero, so we don't need to search for the next 0
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1