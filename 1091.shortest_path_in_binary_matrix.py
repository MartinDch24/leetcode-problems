from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        grid[0][0] = 1
        q = deque([(0, 0)])
        path = 1
        directions = [(-1, -1), (-1, 0),
                      (-1, 1), (0, -1),
                      (0, 1), (1, -1),
                      (1, 0), (1, 1)]

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if (row, col) == (n - 1, n - 1):
                    return path

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 0:
                        q.append((r, c))
                        grid[r][c] = 1

            path += 1

        return -1