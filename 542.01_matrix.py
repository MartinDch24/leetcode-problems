from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        q = deque()
        res = [[0 for _ in range(n)] for _ in range(m)]
        visited = [[False]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = True

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                if 0 <= r+dr < m and 0 <= c+dc < n and not visited[r+dr][c+dc]:
                    visited[r+dr][c+dc] = True
                    res[r+dr][c+dc] = res[r][c] + 1
                    q.append((r+dr, c+dc))

        return res