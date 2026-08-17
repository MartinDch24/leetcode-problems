#Resolved
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dp[i][j] = <the side of the largest square made only of 1s, whoose bottom-right corner is matrix[i-1][j-1]>
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    # For 1 cell to be the bottom-right corner of a square with a side k, there must already be squares with side lengths of at least k-1 on its top, left, and diagonal neighbors.
                    # Therefore, the largest square we can form is limited by the smallest of those three neighboring squares.
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1

                    max_side = max(max_side, dp[i][j])
        return max_side ** 2