from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])  # Rooms to be visited
        visited = {0}   # Visited rooms

        while q:
            node = q.popleft()  # Take the current room out of the queue

            for k in rooms[node]:   # Explore the rooms connected to the current one
                # If the connected room hasn't been visited, append it to the queue
                if k not in visited:
                    visited.add(k)   # Add it to the visited set
                    q.append(k)

        # Check if all rooms have been visited
        return len(visited) == len(rooms)
