#Resolved - 3
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


    #DFS solution with cycle detection:

    #
    # class Solution:
    #     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #         graph = defaultdict(list)
    #
    #         for a, b in prerequisites:
    #             graph[b].append(a)
    #
    #         state = [0] * numCourses  # 0, 1 or 2
    #
    #         def dfs(node):
    #             if state[node] == 1:
    #                 return False  # Cycle detected
    #             elif state[node] == 2:
    #                 return True  # Node has been fully processed, so it is safe
    #
    #             state[node] = 1
    #             for neighbor in graph[node]:
    #                 if not dfs(neighbor):
    #                     return False
    #             state[node] = 2
    #             return True
    #
    #         for i in range(numCourses):
    #             if not dfs(i):
    #                 return False
    #         return True