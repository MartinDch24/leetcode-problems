#Resolved
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

        q = deque()
        res = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # We'll expand from each target, doing BFS on all 0 positions
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for d1, d2 in directions:
                    new_r = r+d1
                    new_c = c+d2

                    if 0 <= new_r < m and 0 <= new_c < n and res[new_r][new_c] == -1:
                        # Inherit and extend distance
                        res[new_r][new_c] = res[r][c] + 1
                        q.append((new_r, new_c))
        return res