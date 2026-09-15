#Resolved - 2
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, w in flights:
            graph[a].append((b, w))

        # total_weight, node, number_of_stops
        heap = [(0, src, 0)]
        # dist[a][b] = <cheapest way to get to node a with b stops>
        dist = [[float('inf') for __ in range(k + 2)] for _ in range(n)]
        dist[src][0] = 0

        while heap:
            total, node, stops = heapq.heappop(heap)

            if node == dst:
                return total
            # If we still haven't reached dst and are at k+1 flights (i.e. k stops)
            if stops > k:
                continue

            for neighbor, price in graph[node]:
                if total + price >= dist[neighbor][stops + 1]:
                    continue
                dist[neighbor][stops + 1] = total + price
                heapq.heappush(heap, (total + price, neighbor, stops + 1))

        return -1