#Resolved
from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)   # node: [neighbor1, ...]
        in_degree = [0] * numCourses    # How many courses need to be taken before course i
        courses_taken = 0

        for a, b in prerequisites:
            graph[b].append(a)  # Course a is dependent on course b
            in_degree[a] += 1   # Course a has +1 course to be taken before it

        q = deque(i for i in range(numCourses) if not in_degree[i]) # We initialize the queue with all independent courses

        while q:
            course = q.popleft()
            courses_taken += 1

            for dependent in graph[course]:
                in_degree[dependent] -= 1   # We take the popped course and deduct it from its neighbor's dependencies
                if in_degree[dependent] == 0:
                    q.append(dependent) # If a course has no more dependencies, we append it to the queue

        return courses_taken == numCourses  # If there are cycles in the graph, courses_taken will be less than numCourses


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