from collections import deque, defaultdict


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)

        for a, b in edges:
            q = [a]
            visited = set()

            while q:
                node = q.pop()

                for neighbor in graph[node]:
                    if neighbor == b:
                        return [a, b]

                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

            graph[a].append(b)
            graph[b].append(a)