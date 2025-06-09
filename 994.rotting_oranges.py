from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        fresh_fruits = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_fruits+=1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if not fresh_fruits:
            return 0

        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh_fruits:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for d1, d2 in directions:
                    if 0 <= r+d1 < m and 0 <= c+d2 < n:
                        if grid[r+d1][c+d2] == 1:
                            grid[r+d1][c+d2] = 2
                            q.append((r+d1, c+d2))
                            fresh_fruits -= 1

        return minutes if fresh_fruits == 0 else -1