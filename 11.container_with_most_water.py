#Resolved
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1

        while l < r:
            # r-l is the width and the shorter height is length of the container
            max_area = max(max_area, (r-l) * min(height[l], height[r]))

            if height[l] < height[r]:   # We always move the shorter line, while shrinking the window, becuase it determines the area of the container
                l += 1
            else:
                r -= 1

        return max_area