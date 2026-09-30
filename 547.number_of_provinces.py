#Resolved - 2
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = n  # Initially every city is a province
        parent = [i for i in range(n)]  # The root of every node (city)
        rank = [1] * n  # Track approximate node tree size, to connected smaller ones to the larger ones

        def find(x):
            while x != parent[x]:
                # Path compression
                parent[x] = parent[parent[x]]
                # Search deeper for the root node
                x = parent[x]
            return x

        def union(a, b):
            nonlocal res

            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                # Connecting the 2 provinces of which a and b are a part of, combines them into 1 province
                # thus reducing the number of provinces by 1
                res -= 1

                # Merge the smaller node tree into the larger one
                if rank[root_a] > rank[root_b]:
                    parent[root_b] = root_a
                elif rank[root_a] < rank[root_b]:
                    parent[root_a] = root_b
                else:
                    parent[root_b] = root_a
                    rank[root_a] += 1

        for i in range(n):
            # The matrix is symmetric and there's no point to process both [i][j] and [j][i]
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    union(i, j)

        return res