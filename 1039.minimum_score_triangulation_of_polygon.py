class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]    # dp[i][j] = smallest triangulation sum of a subpolygon with vertices from i to j inclusive

        # Iterate by increasing subpolygon size
        # Start from triangles (base case) up to the full polygon.
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # We take a triangle with vertices i, j and k from the polygon, which splits it into 2 polygons
                # One with vertices from i to k and the other from k to j
                # We take the cached triangulation sums of those smaller polygons from dp and add the product of the newly formed triangle (i, j and k)
                # We do that for every possible k for k ∈ (i, j) and take the smallest sum
                dp[i][j] = min(
                    dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    for k in range(i+1, j)
                )

        return dp[0][n-1]   # Return the minimum triangulation score for the entire polygon (from vertex 0 to n−1)