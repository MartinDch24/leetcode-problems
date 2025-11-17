class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0]*n for _ in range(n)]  # dp[i][j] = max score Alice can have for stoneValues[i:j+1]

        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]

        for length in range(2, n+1):    # Start from the smallest intervals
            for i in range(n-length+1):
                j = i + length - 1

                for k in range(i, j):   # Take every possible split
                    left_sum = prefix[k+1] - prefix[i]  # Compute the sums of both sides after the split
                    right_sum = prefix[j+1] - prefix[k+1]

                    # Take the smaller side's sum and add the dp of the remaining larger interval
                    if left_sum < right_sum:
                        dp[i][j] = max(dp[i][j], left_sum + dp[i][k])
                    elif left_sum > right_sum:
                        dp[i][j] = max(dp[i][j], right_sum + dp[k+1][j])
                    else:
                        dp[i][j] = max(dp[i][j], left_sum + max(dp[i][k], dp[k+1][j]))

        return dp[0][n-1]