import heapq


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m = len(heights)
        n = len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        min_effort = [[float('inf')] * n for _ in range(m)]
        min_effort[0][0] = 0

        heap = [(0, 0, 0)]  # (effort_so_far, row, col)

        while heap:
            effort, r, c = heapq.heappop(heap)

            if r == m - 1 and c == n - 1:
                return effort

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))

                    if new_effort < min_effort[nr][nc]:
                        min_effort[nr][nc] = new_effort
                        heapq.heappush(heap, (new_effort, nr, nc))


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