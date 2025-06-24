class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        directions = ((1,0), (-1,0), (0,1), (0,-1))

        perimeter = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    perimeter += 4

                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2

                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             for dr, dc in directions:
        #                 nr = i+dr
        #                 nc = j+dc
        #
        #                 if not (0 <= nr < m and 0 <= nc < n):
        #                     perimeter += 1
        #                 elif grid[nr][nc] == 0:
        #                     perimeter += 1
        #
        # return perimeter

