from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        # Directions we can move in
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)]

        n = len(grid)
        q = deque([(0, 0, 1)])  # Enqueue the row and column of the start and the current path length

        while q:
            r, c, length = q.popleft()

            # If we've reached the bottom right corner, return the length we've accumulated
            if r == n-1 and c == n-1:
                return length

            for rd, cd in directions:
                # Check each possible direction we can move in
                # Validate new coordinates and whether it's visited
                if 0 <= r+rd < n and 0 <= c+cd < n and grid[r+rd][c+cd] == 0:
                    grid[r+rd][c+cd] = 1    # Mark the cell as visited
                    q.append((r+rd, c+cd, length+1))    # Append it to the queue

        # If we've processed all cells we can visit and didn't reach grid[n-1][n-1]
        return -1