from collections import deque, defaultdict


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        taken_courses = 0

        for course, req in prerequisites:
            graph[req].append(course)
            in_degree[course] += 1

        q = deque(i for i in range(numCourses) if in_degree[i] == 0)

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                taken_courses += 1

                for course in graph[cur]:
                    in_degree[course] -= 1
                    if in_degree[course] == 0:
                        q.append(course)

        return taken_courses == numCourses

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