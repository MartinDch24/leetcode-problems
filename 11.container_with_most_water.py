#Resolved - 2
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left = 0
        right = n - 1

        while left < right:
            # The height of the container is the height of the shorter bar
            width = min(height[left], height[right]) * (right - left)
            res = max(res, width)

            # Move the shorter bar to try to increase the container height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res