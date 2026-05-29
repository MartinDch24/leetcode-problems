#Resolved
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
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
        # res = 0
        #
        # directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        #
        # def dfs(r, c):
        #     # Mark as visited
        #     grid[r][c] = "0"
        #
        #     for d1, d2 in directions:
        #         new_r = r + d1
        #         new_c = c + d2
        #
        #         if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == "1":
        #             dfs(new_r, new_c)
        #
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1":
        #             res += 1
        #             # Mark all connected parts as visited
        #             dfs(i, j)
        #
        # return res