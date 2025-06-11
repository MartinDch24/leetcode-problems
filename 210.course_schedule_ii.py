from collections import deque, defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        res = []
        q = deque(i for i in range(numCourses) if in_degree[i] == 0)

        while q:
            course = q.popleft()
            res.append(course)

            for dependent in graph[course]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    q.append(dependent)

        return res if len(res) == numCourses else []