class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = ((-1, 0), (0, -1)) # up, left 
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):
                for d1, d2 in directions:
                    r = i+d1
                    c = j+d2
                    if r < 0 or c < 0:
                        continue

                    # The ways to reach grid[i][j] are
                    # the ways to reach its left and top neighbor combined
                    dp[i][j] += dp[r][c]
        
        return dp[m-1][n-1]