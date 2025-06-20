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

    #Union Find solution:
    # n = len(isConnected)
    # parent = list(range(n))
    #
    # def find(x):
    #     root = x
    #     while parent[root] != root:
    #         root = parent[root]
    #     while parent[x] != root:
    #         parent[x], x = root, parent[x]
    #     return root
    #
    # def union(x, y):
    #     rootX = find(x)
    #     rootY = find(y)
    #     if rootX != rootY:
    #         parent[rootY] = rootX
    #
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if isConnected[i][j]:
    #             union(i, j)
    #
    # return len(set(find(i) for i in range(n)))