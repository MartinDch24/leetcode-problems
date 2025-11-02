#Resolved
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        # Prefix sums for every stone
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        # dp[i][j] = max score difference in interval [i, j]
        dp = [[0] * n for _ in range(n)]

        # Build intervals from length 2 up to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]

                # Remove left or right
                # Then remove the optimal move of the next player
                # Then take the largest score difference of both scenarios, since it's most beneficial for a given player to make the difference larger
                dp[i][j] = max(
                    total - stones[i] - dp[i + 1][j],
                    total - stones[j] - dp[i][j - 1]
                )

        return dp[0][n - 1]
