from collections import defaultdict
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))  # The root of each node
        size = [1] * (c + 1)  # Ranks to union groups

        def find(x):  # Return the parent of x and compress the path
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):  # Unite a, b and their groups
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for a, b in connections:  # Build the groups
            union(a, b)

        online = [True] * (c + 1)  # Stations that are online
        min_online = defaultdict(
            list)  # min_online[i] = the station with the smallest id, that is online and connected to i
        res = []  # Results of the queries

        for node in range(1, c + 1):  # Find the smallest id station connected to node
            heapq.heappush(min_online[find(node)], node)

        for action, x in queries:
            if action == 2:
                online[x] = False

            elif action == 1:
                if online[x]:
                    res.append(x)
                    continue

                root = find(x)  # Take the root of the given node
                heap = min_online[root]  # Take all connected station in ascending order by id
                # While the top station is offline, keep popping elements
                while heap and not online[heap[0]]:
                    heapq.heappop(heap)

                # If there was a station found, put in result, otherwise put -1 in
                if heap:
                    res.append(heap[0])
                else:
                    res.append(-1)

        return res