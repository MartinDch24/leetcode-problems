#Resolvedgit pull
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, w in flights:
            graph[a].append([b, w])
        # [<cumulative weight>, <stops so far>, <curr node>]
        heap = [[0, 0, src]]
        # dist[(node, stops)] = <shortest path to node with given stops>
        dist = {(src, 0): 0}
        while heap:
            curr_w, stops, node = heapq.heappop(heap)

            if curr_w > dist.get((node, stops), float('inf')) or stops > k+1:
                continue
            
            # First time we reach dst, is with the shortest distance
            if node == dst:
                return curr_w

            for neighbor, w in graph[node]:
                new_w = curr_w + w
                if new_w < dist.get((neighbor, stops+1), float('inf')):
                    dist[(neighbor, stops+1)] = new_w
                    heapq.heappush(heap, [new_w, stops+1, neighbor])
        
        return -1