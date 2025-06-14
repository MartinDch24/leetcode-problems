class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        directly_connected = set()

        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            directly_connected.add((a, b))
            directly_connected.add((b, a))

        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = degree[i] + degree[j]
                if (i, j) in directly_connected:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank