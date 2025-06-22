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

        #Union Find solution:
        # n = len(edges)
        #
        # parent = [i for i in range(n + 1)]
        # for a, b in edges:
        #     ra = a
        #     while parent[ra] != ra:
        #         parent[ra], ra = parent[parent[ra]], parent[ra]
        #
        #     rb = b
        #     while parent[rb] != rb:
        #         parent[rb], rb = parent[parent[rb]], parent[rb]
        #
        #     if ra == rb:
        #         return [a, b]
        #
        #     parent[ra] = rb