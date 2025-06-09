from collections import deque


class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m = len(maze)
        n = len(maze[0])
        q = deque([(entrance[0], entrance[1], 0)])

        maze[entrance[0]][entrance[1]] = '+'

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            pos1, pos2, steps = q.popleft()

            for d1, d2 in directions:
                if pos1 + d1 >= m or pos1 + d1 < 0 or pos2 + d2 >= n or pos2 + d2 < 0:
                    continue

                if maze[pos1 + d1][pos2 + d2] == '.':
                    if pos1 + d1 == m - 1 or pos1 + d1 == 0 or pos2 + d2 == n - 1 or pos2 + d2 == 0:
                        return steps + 1

                    maze[pos1 + d1][pos2 + d2] = '+'
                    q.append((pos1 + d1, pos2 + d2, steps + 1))

        return -1