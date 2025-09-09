class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1

        res = [0] * (r+1)
        pos = r #   We use pos to fill the resulting list backwards

        while l <= r:
             # Compare the squares of the leftmost and rightmost numbers,
             #because the one on the left might be negative and have a larger square
            if nums[l] ** 2 > nums[r] ** 2:
                res[pos] = nums[l]**2
                l += 1  # Increment the side we square
            else:
                res[pos] = nums[r]**2
                r -= 1

            pos -= 1    # Move down to the next position of the result that needs to be filled in

        return res