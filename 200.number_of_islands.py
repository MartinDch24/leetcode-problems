#Resolved - 2
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

        # Union-Find Solution:

        # m = len(grid)
        # n = len(grid[0])
        #
        # # parent[(i, j)] = <the coordinates of the root piece of land that grid[i][j] is connected to>
        # parent = {(i, j): (i, j) for j in range(n) for i in range(m) if grid[i][j] == '1'}
        # # rank[(i, j)] = <the size rank of the island with root grid[i][j]>
        # rank = {(i, j): 0 for j in range(n) for i in range(m) if grid[i][j] == '1'}
        #
        # res = 0
        #
        # def find(x):
        #     while x != parent[x]:
        #         parent[x] = parent[parent[x]]
        #         x = parent[x]
        #     return x
        #
        # def union(a, b):
        #     nonlocal res
        #     root_a = find(a)
        #     root_b = find(b)
        #
        #     if root_a != root_b:
        #         if rank[root_a] >= rank[root_b]:
        #             parent[root_b] = root_a
        #             rank[root_a] += 1
        #         else:
        #             parent[root_a] = root_b
        #             rank[root_b] += 1
        #         # We increase islands by 1 for every piece of land we find and then decrease them for every 2 islands we connect
        #         res -= 1
        #
        # # Only search for land right and down so we don't try to connect 2 islands twice
        # directions = ((1, 0), (0, 1))
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == '1':
        #             res += 1
        #             for d1, d2 in directions:
        #                 new_r = i + d1
        #                 new_c = j + d2
        #                 if 0 <= new_r < m and 0 <= new_c < n:
        #                     if grid[new_r][new_c] == '1':
        #                         union((i, j), (new_r, new_c))
        # return res