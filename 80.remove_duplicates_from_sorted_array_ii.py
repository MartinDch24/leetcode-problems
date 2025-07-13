class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) < 2:  # We make sure the array has at least 2 numbers
            return 1

        write = 2  # Write is the index we'll be overwriting and the length of the new array
        for i in range(2, len(nums)):
            if nums[i] != nums[write - 2]:  # If the current number isn't a 3rd instance, we continue the new array with it and increment write to continue moving on
                nums[write] = nums[i]
                write += 1

        return write
