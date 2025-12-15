from collections import defaultdict


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        col = defaultdict(list) # All ys with coordinate x
        row = defaultdict(list) # All xs with coordinate y

        for x, y in buildings:
            col[x].append(y)
            row[y].append(x)

        uncovered = set()   # All buildings that are not covered

        for x in col:
            min_y = min(col[x])
            max_y = max(col[x])
            # Add the top and bottom building on col x
            uncovered.add((x, min_y))
            uncovered.add((x, max_y))

        for y in row:
            min_x = min(row[y])
            max_x = max(row[y])
            # Add the leftmost and rightmost building on row y
            uncovered.add((min_x, y))
            uncovered.add((max_x, y))

        # All covered building are the total buildings - the uncovered ones
        return len(buildings) - len(uncovered)