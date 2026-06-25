import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        Treat time as edge weights. Every time we want to move, the total weight becomes max(current_time, time_of_new_cell)
        '''
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        m = len(grid)
        n = len(grid[0])

        heap = [(grid[0][0], 0, 0)]
        dist = {(0, 0): grid[0][0]}

        while heap:
            time, r, c = heapq.heappop(heap)

            if r == m-1 and c == n-1:
                return time

            if time > dist.get((r, c), float('inf')):
                continue

            for d1, d2 in directions:
                new_r = r+d1
                new_c = c+d2
                if 0 <= new_r < m and 0 <= new_c < n:
                    new_time = max(grid[new_r][new_c], time)
                    if new_time  < dist.get((new_r, new_c), float('inf')):
                            dist[(new_r, new_c)] = new_time
                            heapq.heappush(heap, (new_time, new_r, new_c))