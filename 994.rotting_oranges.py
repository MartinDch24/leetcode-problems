#Resolved - 3
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        queue = deque([])
        minutes = 0
        oranges_left = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    oranges_left += 1

        # Do BFS, expanding from each rotten orange layer by layer, with every layer being 1 minute
        while queue and oranges_left:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for d1, d2 in directions:
                    new_r, new_c = r + d1, c + d2
                    if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        oranges_left -= 1
                        queue.append((new_r, new_c))

        return minutes if not oranges_left else -1