import heapq
import math
from collections import defaultdict


class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            prob = succProb[i]
            if prob == 0.0:
                continue
            log_prob = math.log(prob)
            graph[a].append((b, log_prob))
            graph[b].append((a, log_prob))

        heap = [(-0.0, start_node)]
        best = [-float('inf')] * n
        best[start_node] = 0.0

        while heap:
            curr_log_prob_neg, node = heapq.heappop(heap)
            curr_log_prob = -curr_log_prob_neg

            if node == end_node:
                return math.exp(curr_log_prob)

            for neighbor, edge_log_prob in graph[node]:
                new_log_prob = curr_log_prob + edge_log_prob
                if new_log_prob > best[neighbor]:
                    best[neighbor] = new_log_prob
                    heapq.heappush(heap, (-new_log_prob, neighbor))

        return 0.0