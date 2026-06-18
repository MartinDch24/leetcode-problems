from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []

        # Build graph with weight on edges
        for i, pair in enumerate(equations):
            a, b = pair
            graph[a].append([b, values[i]])
            graph[b].append([a, 1/values[i]])

        for a, b in queries:
            # Check for non-existant nodes
            if a not in graph or b not in graph:
                res.append(-1.0)
                continue
            
            # Do DFS on the start node(a), looking for the end one(b)
            stack = [[a, 1]]
            visited= {a}
            total_weight = 1
            found = False
            while stack:
                var, curr_w = stack.pop()

                if var == b and var in graph:
                    total_weight = curr_w
                    found = True

                for neighbor, weight in graph[var]:
                    if neighbor not in visited:
                        stack.append([neighbor, curr_w * weight])
                        visited.add(neighbor)

            res.append(total_weight if found else -1.0)

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