#Resolved
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0    # Leftmost index
        right = len(nums)-1     # Rightmost index

        while left <= right:
            mid = (left + right) // 2

            # Reduce right boundary if nums[mid] overshoots the target
            # Otherwise increase the left boundary, so nums[mid] can reach target
            if target <= nums[mid]:
                right = mid-1
            else:
                left = mid+1

        return left # Last valid position for target to be insterted