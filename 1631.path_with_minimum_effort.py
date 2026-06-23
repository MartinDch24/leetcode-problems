#Resolved
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        heap = [[0, 0, 0]]  # Store route effort, row and col for each unfinished node
        dist = {(0, 0): 0}  # dist[node] = minimum effort found so far to reach this node
        while heap:
            curr_eff, r, c = heapq.heappop(heap)
            if curr_eff > dist.get((r, c), float('inf')):
                continue
            
            for d1, d2 in directions:
                new_r = r+d1
                new_c = c+d2
                if 0 <= new_r < m and 0 <= new_c < n:
                    new_eff = max(curr_eff, abs(heights[r][c] - heights[new_r][new_c]))
                    if new_eff < dist.get((new_r, new_c), float('inf')):
                        dist[(new_r, new_c)] = new_eff
                        heapq.heappush(heap, [new_eff, new_r, new_c])
            
        return dist[(m-1, n-1)]


        #Union Find solution:
        # m = len(heights)
        # n = len(heights[0])
        # parent = list(range(m * n))
        #
        # def find(x):
        #     while x != parent[x]:
        #         parent[x] = parent[parent[x]]
        #         x = parent[x]
        #     return x
        #
        # def union(x, y):
        #     parent[find(x)] = find(y)
        #
        # edges = []
        # for r in range(m):
        #     for c in range(n):
        #         i = r * n + c  # flatten (r, c) to a 1D index for Union Find
        #         if r + 1 < m:
        #             edges.append((abs(heights[r][c] - heights[r + 1][c]), i, (r + 1) * n + c))
        #         if c + 1 < n:
        #             edges.append((abs(heights[r][c] - heights[r][c + 1]), i, r * n + (c + 1)))
        #
        # edges.sort()
        #
        # #connect edges starting from the least effort ones, until we've connected (0, 0) and (m-1, n-1)
        # for effort, u, v in edges:
        #     union(u, v)
        #     if find(0) == find(m * n - 1):
        #         return effort
        #
        # return 0