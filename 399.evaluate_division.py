from collections import deque, defaultdict


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)

        for i, edge in enumerate(equations):
            a, b = edge
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        res = []

        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1)
                continue
            if start == end:
                res.append(1)
                continue

            q = deque([(start, 1)])
            visited = {start}
            found = False

            while q and not found:
                node, curr_weight = q.popleft()

                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        if neighbor == end:
                            res.append(curr_weight * weight)
                            found = True
                            break

                        visited.add(neighbor)
                        q.append((neighbor, curr_weight * weight))

            if not found:
                res.append(-1)

        return res

        #Iterative DFS solution:
        # graph = defaultdict(list)
        #
        # for i, edge in enumerate(equations):
        #     a, b = edge
        #     graph[a].append((b, values[i]))
        #     graph[b].append((a, 1 / values[i]))
        #
        # res = []
        #
        # for start, end in queries:
        #     if start not in graph or end not in graph:
        #         res.append(-1)
        #         continue
        #     if start == end:
        #         res.append(1)
        #         continue
        #
        #     s = [(start, 1)]
        #     visited = {start}
        #     found = False
        #
        #     while s and not found:
        #         node, curr_weight = s.pop()
        #
        #         for neighbor, weight in graph[node]:
        #             if neighbor not in visited:
        #                 if neighbor == end:
        #                     res.append(curr_weight * weight)
        #                     found = True
        #                     break
        #
        #                 visited.add(neighbor)
        #                 s.append((neighbor, curr_weight * weight))
        #
        #     if not found:
        #         res.append(-1)
        #
        # return res