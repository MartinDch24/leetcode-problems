#Resolved
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix[0])
        # We aim to collapse the grid, so we can turn the problem into 84. Largest Rectangle in Histogram
        heights = [0] * (m + 1)  # Add an extra 0, so the stack can be emptied at the end of processing each row

        max_area = 0
        for row in matrix:
            # Find how many consecutive 1s we have in each column
            for j, num in enumerate(row):
                if num == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []  # Monotonic increasing stack of indices
            for j in range(m + 1):
                # We end the width of a rectangle at heights[j-1]
                while stack and heights[stack[-1]] > heights[j]:
                    idx = stack.pop()

                    # heights[stack[-1]] is the first height on the left, smaller than heights[idx], so heights[stack[-1]+1] is the start of the width
                    width = j - stack[-1] - 1 if stack else j
                    area = width * heights[idx]
                    max_area = max(max_area, area)
                stack.append(j)

        return max_area