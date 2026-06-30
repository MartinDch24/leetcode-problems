#Resolved
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        # Rank trees by height
        rank = [0 for _ in range(n)]
        provinces = set()

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(a, b):
            root_a = find(a)
            root_b = find(b)
                
            if root_a != root_b:
                # Merge the smaller tree into the larger one
                if rank[root_a] > rank[root_b]:
                    parent[root_b] = root_a
                elif rank[root_a] < rank[root_b]:
                    parent[root_a] = root_b
                else:
                    parent[root_b] = root_a
                    rank[root_a] += 1

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i, j)

        # The provinces are a set of each node's root, so we return its length
        return len({find(i) for i in range(n)})