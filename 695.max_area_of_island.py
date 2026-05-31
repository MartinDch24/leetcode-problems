class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        res = 0

        # Returns the area of each island
        def dfs(r, c):
            # Mark as visited
            grid[r][c] = 0
            area = 1

            for d1, d2 in directions:
                new_r = r + d1
                new_c = c + d2

                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                    area += dfs(new_r, new_c)

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res