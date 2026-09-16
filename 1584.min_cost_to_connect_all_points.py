from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = defaultdict(tuple)  # Use the x and y coords of the points as their names
        rank = defaultdict(int)

        def find(x_y):
            while x_y != parent[x_y]:
                parent[x_y] = parent[parent[x_y]]
                x_y = parent[x_y]
            return x_y

        def union(coords1, coords2):
            root_1 = find(coords1)
            root_2 = find(coords2)

            if root_1 != root_2:
                if rank[root_1] > rank[root_2]:
                    parent[root_2] = root_1
                    rank[root_1] += 1
                else:
                    parent[root_1] = root_2
                    rank[root_2] += 1
                return False
            else:
                return True

        heap = []
        for i, (xi, yi) in enumerate(points):
            parent[(xi, yi)] = (xi, yi)
            # Skip building duplicate edges
            for xj, yj in points[i + 1:]:
                dist = abs(xi - xj) + abs(yi - yj)
                # Process cheapest edges first
                heapq.heappush(heap, (dist, (xi, yi), (xj, yj)))

        total_weight = 0
        edges = 0
        point_count = len(parent)

        while heap:
            weight, start_coords, end_coords = heapq.heappop(heap)
            # Skip already connected components
            if union(start_coords, end_coords):
                continue

            edges += 1
            total_weight += weight

            # The edges between n points will always be n-1
            if edges == point_count - 1:
                return total_weight

        return total_weight