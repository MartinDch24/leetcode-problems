#Resolved - 2
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time = 0
        fresh = 0

        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        while queue and fresh:
            time += 1
            # For each minute explore the area only adjacent to current rotten oranges
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for d1, d2 in directions:
                    new_r = r + d1
                    new_c = c + d2

                    if 0 <= new_r < m and 0 <= new_c < n:
                        if grid[new_r][new_c] == 1:
                            grid[new_r][new_c] = 2
                            queue.append((new_r, new_c))
                            fresh -= 1

        return -1 if fresh else time
