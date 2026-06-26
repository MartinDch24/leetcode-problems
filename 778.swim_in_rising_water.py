#Resolved
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # The cost of a path is the maximum elevation encountered so far.
        
        m = len(grid)
        n = len(grid[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        heap = [(grid[0][0], 0, 0)]
        visited = set()

        while heap:
            t, r, c = heapq.heappop(heap)

            # Add to visited only after popping, so the best path can be found
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # Min-heap guarantess the first time we arrive at the bottom-right cell, it will be through the most efficient path
            if r == m-1 and c == n-1:
                return t

            for d1, d2 in directions:
                new_r = r+d1
                new_c = c+d2
                if 0 <= new_r < m and 0 <= new_c < n:
                    new_t = max(t, grid[new_r][new_c])
                    if (new_r, new_c) not in visited:
                        heapq.heappush(heap, (new_t, new_r, new_c))