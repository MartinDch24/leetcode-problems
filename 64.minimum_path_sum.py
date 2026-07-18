#Resolved
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # up, left
        directions = ((-1, 0), (0, -1))

        # dp[i][j] = <smallest cost to reach grid[i][j]
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                for d1, d2 in directions:
                    r = i+d1
                    c = j+d2
                    if 0 <= r and 0 <= c:
                        dp[i][j] = min(dp[r][c] + grid[i][j], dp[i][j])
        
        return dp[m-1][n-1]