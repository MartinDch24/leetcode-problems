class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        x1, y1 = points[0]

        for x2, y2 in points[1:]:
            # The fastest time will be with as many diagonals as possible because they allow us to move both vertically and horizontally in the same second
            # The differences between x1 and x2 and y1 and y2 are the distances between the 2 points on the x and y axises
            # If that difference is for example 5 for x and 3 for y, then we can take 3 diagonals and move 2 times on x, which is equal to the larger difference - 5
            time += max(abs(x1 - x2), abs(y1 - y2))
            x1, y1 = x2, y2

        return time