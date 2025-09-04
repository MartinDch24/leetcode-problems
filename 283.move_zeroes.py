class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0 # The position the first found non-zero should go

        for i in range(n):
            if nums[i] != 0:
                # When we find a non-zero, we put it at pos, increment pos and replace the current position nums[i] with a zero
                # This way, all of the 0s will get pushed to the back
                nums[i], nums[pos] = 0, nums[i]
                pos += 1

        #First solution:
        # n = len(nums)
        # pos = 0 # The position the first found non-zero should go
        #
        # for i in range(n):
        #     if nums[i] != 0:    # When we find a non-zero, we put it at pos and increment pos
        #         nums[pos] = nums[i]
        #         pos += 1
        #
        # while pos < n:  # If pos is less than len(nums), that means that we should put the 0 we overwrote earlier at nums[pos] and increment it, until we have filled the array
        #     nums[pos] = 0
        #     pos += 1