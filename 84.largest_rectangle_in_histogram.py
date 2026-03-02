class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Add a 0 at the end, so we can empty out the stack before ending the loop
        max_area = 0

        stack = []
        for i in range(len(heights)):
            # We are looking for the first smaller height on the right of heights[stack[-1]]
            while stack and heights[stack[-1]] > heights[i]:
                idx = stack.pop()

                # stack[-1] is the first smaller than heights[idx] height on the left
                # The rectangle's width is from that left boundary to the right one
                # which are stack[-1] + 1 and i - 1
                # (i - 1) - (stack[-1] + 1) + 1
                width = i - stack[-1] - 1 if stack else i

                # We are essentially spreading out heights[idx] until we reach the left and right boundaries, to make the largest possible ractangle with it
                area = width * heights[idx]
                max_area = max(max_area, area)
            stack.append(i)

        return max_area