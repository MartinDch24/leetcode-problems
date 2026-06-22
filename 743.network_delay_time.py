from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a, b, w in times:
            graph[a].append([b, w])

        # Keep nodes with the smallest total weight to them at the top
        heap = [[0, k]]
        dist = {k: 0}   # dist[node] = shortest distance from k to node

        while heap:
            curr_w, node = heapq.heappop(heap)
            
            # Skip less efficient paths
            if curr_w > dist.get(node, float('inf')):
                continue
 
            for neighbor, w in graph[node]:
                new_w = curr_w + w

                if new_w < dist.get(neighbor, float('inf')):
                    dist[neighbor] = new_w
                    heapq.heappush(heap, (new_w, neighbor))

        # All nodes are visited, only if all of them are in dist
        return max(dist.values()) if len(dist) == n else -1