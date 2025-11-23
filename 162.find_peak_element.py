class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            # If the current number if less then, the right one, the peak is to the right
            # Otherwise it's to the left
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid

        return left