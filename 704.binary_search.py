#Resolved
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0  # Smallest possible index
        right = len(nums) - 1  # Largest possible index

        while left <= right:
            mid = (left + right) // 2  # The value in the middle of left and right

            # If nums[mid] < target, move up left, to get a larger mid
            if nums[mid] < target:
                left = mid + 1
            # If it's > target, move down right, to make mid smaller
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        # If we can't find target within the array, then left eventually becomes larger than right and we return -1
        return -1
