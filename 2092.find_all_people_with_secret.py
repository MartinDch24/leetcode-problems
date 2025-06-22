from collections import defaultdict, deque


class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        time_table = defaultdict(list)
        enlightened = set([0, firstPerson])

        for a, b, time in meetings:
            time_table[time].append((a, b))

        for time in sorted(time_table.keys()):
            edges = time_table[time]

            curr_graph = defaultdict(list)
            for a, b in edges:
                curr_graph[a].append(b)
                curr_graph[b].append(a)

            q = deque([p for p in curr_graph.keys() if p in enlightened])

            while q:
                node = q.popleft()

                for neighbor in curr_graph[node]:
                    if neighbor not in enlightened:
                        enlightened.add(neighbor)
                        q.append(neighbor)

        return list(enlightened)
