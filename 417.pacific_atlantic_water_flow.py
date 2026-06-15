#Resolved
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        pacific = set()
        atlantic = set()

        stack = []

        # Add all cells on the left and top borders to the pacific set
        for i in range(m):
            if i == 0:
                for j in range(n):
                    pacific.add((i, j))
                    stack.append([i, j])
            else:
                pacific.add((i, 0))
                stack.append([i, 0])

        # Do DFS on pacific cells
        while stack:
            r, c = stack.pop()

            for d1, d2 in directions:
                new_r = r + d1
                new_c = c + d2

                if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in pacific:
                    if heights[new_r][new_c] >= heights[r][c]:
                        pacific.add((new_r, new_c))
                        stack.append([new_r, new_c])

        # Add all cells on the right and bottom borders to the atlantic set
        for i in range(m):
            if i == m - 1:
                for j in range(n):
                    atlantic.add((i, j))
                    stack.append([i, j])
            else:
                atlantic.add((i, n - 1))
                stack.append([i, n - 1])

        # Do DFS on the atlantic cells
        while stack:
            r, c = stack.pop()

            for d1, d2 in directions:
                new_r = r + d1
                new_c = c + d2

                if 0 <= new_r < m and 0 <= new_c < n and (new_r, new_c) not in atlantic:
                    if heights[new_r][new_c] >= heights[r][c]:
                        atlantic.add((new_r, new_c))
                        stack.append([new_r, new_c])

        # Inner join the pacific and atlantic sets
        return list(pacific & atlantic)