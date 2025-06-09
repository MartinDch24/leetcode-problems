import heapq


class Solution(object):
    def minimumTime(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        # (time, x, y)
        heap = [(0, 0, 0)]  # Start at (0,0) at time 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True

            if x == n - 1 and y == m - 1:
                return time  # Reached the goal

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    wait_time = grid[nx][ny]
                    arrival = time + 1

                    if arrival < wait_time:
                        # We must wait for the room to unlock
                        # But we may need to wait an *even* number of seconds to enter
                        # because entering at odd/even second might not be allowed
                        delay = wait_time - arrival
                        if delay % 2 == 1:
                            arrival = wait_time + 1
                        else:
                            arrival = wait_time
                    heapq.heappush(heap, (arrival, nx, ny))

        return -1