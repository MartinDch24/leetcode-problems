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