class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n  # The tallest bar to the left of height[i]
        max_right = [0] * n # The tallest bar to the right of heigh[i]
        res = 0

        curr_max = 0    # The tallest bar so far
        for i in range(n):
            max_left[i] = curr_max
            curr_max = max(curr_max, height[i])

        curr_max = 0
        for i in range(n-1, -1, -1):
            max_right[i] = curr_max
            curr_max = max(curr_max, height[i])

        for i in range(n):
            # For each block, take the shorter of the tallest bars on the right and left, subtract their heights and add it to the total water count
            trapped = min(max_left[i], max_right[i]) - height[i]
            if trapped > 0:
                res += trapped

        return res

        #Two-pointer solution:

        # n = len(height)
        # left, right = 0, n - 1
        # max_left, max_right = 0, 0
        # res = 0
        #
        # # Initialize a window from the start of the array to the end and shrink it
        # while left < right:
        #     if height[left] < height[right]:
        #         # If the left side is the shorter one, we see if it's the tallest we've seen yet on the left and update accordingly
        #         if height[left] >= max_left:
        #             max_left = height[left]
        #         else:
        #             # If it isn't the tallest we've seen, that means there's trapped water and the volume is max_left - the current left
        #             res += max_left - height[left]
        #         left += 1  # Shrink the window from the left
        #     else:
        #         # If the left side is the taller one, we do the same for the right
        #         if height[right] >= max_right:
        #             max_right = height[right]
        #         else:
        #             res += max_right - height[right]
        #         right -= 1
        #
        # return res