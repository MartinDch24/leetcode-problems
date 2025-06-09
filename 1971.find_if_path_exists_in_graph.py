from collections import deque, defaultdict


class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)

        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)

        q = deque([source])
        visited = set()

        while q:
            node = q.popleft()

            if node in visited:
                continue

            if node == destination:
                return True

            visited.add(node)

            for neighbour in graph[node]:
                q.append(neighbour)

        return False