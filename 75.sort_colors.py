class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We use left to track the color after the last 0
        # and right to track the color before the first 2
        # This way we can move all 0s to the left and 2s to right, so only the 1s are left in the middle
        left, right = 0, len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
                continue  # We don't increment after swapping a 2, because we don't know what the current value of nums[i] now is

            i += 1