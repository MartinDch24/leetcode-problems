from collections import deque


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = set()
        provinces = 0

        for i in range(n):
            if i not in visited:
                provinces += 1
                q = deque([i])

                while q:
                    city = q.popleft()
                    visited.add(city)

                    for j in range(n):
                        if isConnected[city][j] and j not in visited:
                            q.append(j)

        return provinces