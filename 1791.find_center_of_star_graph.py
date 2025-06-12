class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a, b = edges[0]
        c, d = edges[1]

        if a == c or a == d:
            return a
        return b

        # n = max(max(edges, key=lambda x: max(x)))
        # connected = [0] * (n+1)

        # for a, b in edges:
        #     connected[a] += 1
        #     connected[b] += 1

        # for i in range(1, n + 1):
        #     if connected[i] == n - 1:
        #         return i