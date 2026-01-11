#Resolved
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:    # No duplicates if there aren't any numbers
            return 0

        i = 0   # The indices of the unique numbers
        for j in range(1, len(nums)):
            # Each time we find a unique number, we place it next to the previous unique one
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1    # Add 1, because i is an index and we want a count