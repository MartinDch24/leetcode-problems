class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:  # If the starting cell is an obstacle, we can't move
            return 0

        paths = [[0] * m for _ in range(n)]  # paths[i][j] = ways to reach obstacleGrid[i][j]
        paths[0][0] = 1  # We have 1 way to reach the starting cell

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    # We want i and j to be more than 0, because otherwise i-1 or j-1 won't be valid indices
                    if i > 0:
                        paths[i][j] += paths[i - 1][j]
                    if j > 0:
                        paths[i][j] += paths[i][j - 1]

        return paths[n - 1][m - 1]