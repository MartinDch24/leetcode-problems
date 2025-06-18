from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q = deque([0])
        visited = {0}

        while q:
            node = q.popleft()

            for neighbor in rooms[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return len(visited) == len(rooms)