from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        stack = [c for c in range(numCourses) if indegree[c] == 0]
        while stack:
            curr = stack.pop()
            res.append(curr)

            for course in graph[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    stack.append(course)

        return res if len(res) == numCourses else []