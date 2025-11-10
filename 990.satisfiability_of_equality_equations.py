class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        let_to_idx = {chr(i + ord('a')): i for i in range(26)}  # {'a': 0, 'b': 1, ...}
        parent = list(range(26))    # parent[x] = the root node of node x
        size = [1] * 26 # The size of the tree of each root

        def find(x):    # Find the root parent of x and compress the path to it
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            # The root of a and the root of b
            ra, rb = find(a), find(b)

            if ra == rb:
                return

            # Swap so ra is the larger tree
            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        # Build the graph with only the equal equations
        for eq in equations:
            if eq[1] == "=":
                a = let_to_idx[eq[0]]
                b = let_to_idx[eq[3]]

                union(a, b)

        # Check whether nodes that shouldn't be connected, actually are
        for eq in equations:
            if eq[1] == "!":
                a = let_to_idx[eq[0]]
                b = let_to_idx[eq[3]]

                if find(a) == find(b):
                    return False

        return True