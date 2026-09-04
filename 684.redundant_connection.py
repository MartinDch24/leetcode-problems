# Resolved - 2
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

        # Union Find solution:
            # class Solution:
            #     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
            #         parent = [x for x in range(len(edges) + 1)]
            #
            #         def find(x):
            #             while parent[x] != x:
            #                 # Compress path
            #                 parent[x] = parent[parent[x]]
            #                 # Continue looking for the root
            #                 x = parent[parent[x]]
            #             return x
            #
            #         def union(a, b):
            #             if find(a) == find(b):
            #                 return True
            #
            #             root_a = find(a)
            #             root_b = find(b)
            #             parent[root_a] = root_b
            #
            #         for a, b in edges:
            #             if union(a, b):
            #                 return [a, b]