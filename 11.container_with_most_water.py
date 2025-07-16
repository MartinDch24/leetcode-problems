class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_area = 0  # Largest container so far

        l = 0  # Left index
        r = n - 1  # Right index

        while l <= r:
            new_area = min(height[l], height[r]) * (
                        r - l)  # We take the shorter line and multiply it by the distance to get the water the conatiner can have

            max_area = max(max_area, new_area)

            if height[l] < height[
                r]:  # We take the shorter line thus far and move towards the inside, since moving the longer line could cause us to loose out on potential area
                l += 1
            else:
                r -= 1

        return max_area