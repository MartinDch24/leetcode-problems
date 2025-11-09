from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)

        parent = list(range(n))  # The root of each nood
        size = [1] * n  # The size of the tree of a given root

        def find(x):
            # Return the parent of x and compress the path to it
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            # Get the roots of a and b
            ra, rb = find(a), find(b)

            if ra == rb:
                return

            # Make the root of a, the larger tree and unite them
            if size[ra] < size[rb]:
                ra, rb = rb, ra

            parent[rb] = ra
            size[ra] += size[rb]

        # Build the connections
        for a, b in pairs:
            union(a, b)

        # All groups of connected components
        components = defaultdict(list)
        # The new string
        res = [''] * n

        # Add each index to its group
        for i in range(n):
            components[find(i)].append(i)

        # Take the indeces of each group
        for comp in components.values():

            # Order the indexec by their letter's lexicographical value
            ordered_comp = sorted(comp, key=lambda x: s[x])

            # i is the index in the new string and j the best letter to go in its place
            for i, j in zip(comp, ordered_comp):
                res[i] = s[j]

        return "".join(res)