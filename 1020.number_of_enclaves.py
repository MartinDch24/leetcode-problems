from collections import deque


class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        q = deque()

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(m):
            if grid[i][0] == 1:
                q.append((i, 0))
                grid[i][0] = 0
            if grid[i][n-1] == 1:
                q.append((i, n-1))
                grid[i][n-1] = 0

        for j in range(n):
            if grid[0][j] == 1:
                q.append((0, j))
                grid[0][j] = 0
            if grid[m-1][j] == 1:
                q.append((m-1, j))
                grid[m-1][j] = 0

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and grid[r+dr][c+dc] == 1:
                    grid[r+dr][c+dc] = 0
                    q.append((r+dr, c+dc))

        return sum(cell for row in grid for cell in row)