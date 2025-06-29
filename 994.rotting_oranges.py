#Resolved
from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()  # We use a queue so we can do BFS
        fresh = 0
        minutes = 0

        m = len(grid)
        n = len(grid[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))  # Directions in which we can move

        for i in range(m):  # We iterate through every cell
            for j in range(n):
                if grid[i][j] == 1:  # If we find a 1, we add to the fresh oranges
                    fresh += 1
                elif grid[i][j] == 2:  # If we find a 2, we add it to the queue
                    q.append((i, j))

        while q and fresh:
            minutes += 1  # We add a minute for each iteration of the while loop
            for _ in range(len(q)):  # We go through every rotten orange for the given minute
                r, c = q.popleft()

                for dr, dc in directions:  # Check each direction of the rotten orange
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:  # Check if the indexes are in range
                        if grid[nr][nc] == 1:  # If we find a fresh orange, we make it rotten and deduct from fresh
                            fresh -= 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))

        return minutes if fresh == 0 else -1  # If we have gone through every rotten orange in the queue without getting rid of all fresh ones, we return -1