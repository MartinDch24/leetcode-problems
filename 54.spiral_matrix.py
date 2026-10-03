class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        top, bottom = 0, m-1
        start, end = 0, n-1

        while len(res) < m*n:
            for i in range(top, bottom+1):
                if i == top:
                    for j in range(start, end+1):
                        res.append(matrix[i][j])
                else:
                    res.append(matrix[i][end])
            end -= 1
            top += 1

            if start <= end:
                for i in range(bottom, top-1, -1):
                    if i == bottom:
                        for j in range(end, start-1, -1):
                            res.append(matrix[i][j])
                    else:
                        res.append(matrix[i][start])
            start += 1
            bottom -= 1

        return res