from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        islands = 0
        q = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    islands += 1
                    q = deque()
                    q.append((i, j))
                    grid[i][j] = "0"

                    while q:
                        r, c = q.popleft()
                        for d1, d2 in directions:
                            if 0<= r+d1 <m and 0<= c+d2 <n and grid[r+d1][c+d2] == "1":
                                q.append((r+d1, c+d2))
                                grid[r+d1][c+d2] = "0"

        return islands

        # m = len(grid)
        # n = len(grid[0])
        #
        # islands = 0
        #
        # def dfs(r, c):
        #     stack = [(r, c)]
        #     while stack:
        #         r, c = stack.pop()
        #         if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
        #             grid[r][c] = "0"
        #             stack.append((r + 1, c))
        #             stack.append((r - 1, c))
        #             stack.append((r, c + 1))
        #             stack.append((r, c - 1))
        #
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1":
        #             islands += 1
        #             dfs(i, j)
        #
        # return islands