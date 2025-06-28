#Resolved
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

        for i, edge in enumerate(edges):
            a, b = edge
            prob = succProb[i]

            if prob == 0.0:  # log(0) is undefined
                continue

            log_of_prob = math.log(prob)  # We use natural logarithms for better end result precision
            graph[a].append((b, log_of_prob))
            graph[b].append((a, log_of_prob))

        heap = [(0.0, start_node)]  # We start with the starting node and a probability of 1, the log of which is 0
        max_prob = [-float('inf')] * n
        max_prob[start_node] = 0.0

        while heap:
            curr_prob_neg, node = heapq.heappop(heap)
            curr_prob = -curr_prob_neg  # Convert the probability back to normal

            if node == end_node:
                return math.exp(curr_prob)  # We return the exponent of the maximum probability

            for neighbor, prob in graph[node]:
                new_prob = curr_prob + prob  # log(a) + log(b) = log(a*b)

                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(heap, (-new_prob, neighbor))

                    # We save the probability as a negative so the priority queue can be max priority, instead of min

        return 0.0