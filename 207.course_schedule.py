#Resolved - 2
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depend = [0] * numCourses  # depend[c] = <how many courses to take before you can take c>
        graph = defaultdict(list)  # graph[a] = b -> edge from a to b
        taken = 0

        for a, b in prerequisites:
            graph[b].append(a)
            depend[a] += 1

        stack = [course for course in range(numCourses) if depend[course] == 0]
        while stack:
            curr = stack.pop()
            taken += 1

            for course in graph[curr]:
                depend[course] -= 1
                if depend[course] == 0:
                    stack.append(course)

        return taken == numCourses


    #Iterative DFS solution with cycle detection:
    # graph = defaultdict(list)
    # visited = [0] * numCourses
    #
    # for course, req in prerequisites:
    #     graph[req].append(course)
    #
    # for course in range(numCourses):
    #     if visited[course] != 0:
    #         continue
    #
    #     s = [(course, iter(graph[course]))]
    #
    #     while s:
    #         node, neighbors = s[-1]
    #
    #         try:
    #             neighbor = neighbors.next()
    #
    #             if visited[neighbor] == 0:
    #                 visited[neighbor] = 1
    #                 s.append((neighbor, iter(graph[neighbor])))
    #
    #             elif visited[neighbor] == 1:
    #                 return False
    #
    #         except StopIteration:
    #             visited[node] = 2
    #             s.pop()
    #
    # return True