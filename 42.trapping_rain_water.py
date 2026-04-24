#Resolved
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n  # The tallest bar to the left of height[i]
        max_right = [0] * n # The tallest bar to the right of height[i]
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

        # left, right = 0, len(height) - 1
        # max_left = max_right = 0  # Tallest heights, moving from the left and moving from the right
        # res = 0
        #
        # while left < right:
        #     if height[left] < height[right]:
        #         max_left = max(max_left, height[left])
        #         # height[left] <= max_left and it can trap water up to max_left height
        #         res += max_left - height[left]
        #         left += 1
        #     else:
        #         # Same logic
        #         max_right = max(max_right, height[right])
        #         res += max_right - height[right]
        #         right -= 1
        # return res

        #Monotonic Stack solution:

        # res = 0
        #
        # stack = []  # Store descending heights
        # for i in range(len(height)):
        #     while stack and height[stack[-1]] < height[i]:
        #         idx = stack.pop()
        #         if not stack:
        #             break
        #
        #         bottom = height[idx]  # The height of the bottom of the container
        #         left = height[stack[-1]]  # The height of the left wall
        #         right = height[i]  # The height of the right wall
        #         # <the height of the trapped water> * <the width it spans>
        #         res += (min(left, right) - bottom) * (i - stack[-1] - 1)
        #     stack.append(i)
        #
        # return res