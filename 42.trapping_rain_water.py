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