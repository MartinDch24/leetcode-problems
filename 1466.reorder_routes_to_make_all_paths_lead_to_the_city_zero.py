from collections import deque, defaultdict


class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = [False] * n
        flips = 0

        q = deque([0])
        visited[0] = True

        while q:
            curr = q.popleft()

            for neighbor, needs_flip in graph[curr]:
                if not visited[neighbor]:
                    flips += needs_flip
                    visited[neighbor] = True
                    q.append(neighbor)

        return flips