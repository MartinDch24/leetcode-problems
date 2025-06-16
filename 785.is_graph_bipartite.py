from collections import deque


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [-1] * n

        for i in range(n):
            if colors[i] == -1:
                q = deque([i])
                colors[i] = 0

                while q:
                    node = q.popleft()

                    for neighbour in graph[node]:
                        if colors[neighbour] == -1:
                            colors[neighbour] = 1 - colors[node]
                            q.append(neighbour)
                        elif colors[neighbour] == colors[node]:
                            return False

        return True