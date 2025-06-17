from collections import deque


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        q = deque([(0, [0])])
        paths = []

        while q:
            node, path = q.popleft()

            for neighbor in graph[node]:
                if neighbor == n - 1:
                    paths.append(path + [neighbor])
                else:
                    q.append((neighbor, path + [neighbor]))

        return paths