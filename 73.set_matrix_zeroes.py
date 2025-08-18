#Resolved
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []  # Coordinates of 0s we find
        m = len(matrix)  # Column length
        n = len(matrix[0])  # Row length

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))  # When we find a 0, we save it's coordinates

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))  # right, left, up, down

        for r, c in zeroes:
            for i in range(
                    m):  # For every column coordinate, we 0 out the whole row, by iterating through every row index
                matrix[i][c] = 0
            for j in range(n):  # Same idea but with the row index and iterating through every column index
                matrix[r][j] = 0


# class Solution(object):
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         rows = len(matrix)
#         cols = len(matrix[0])
#         first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
#         first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
#
#         for i in range(rows):
#             for j in range(cols):
#                 if matrix[i][j] == 0:
#                     matrix[0][j] = 0
#                     matrix[i][0] = 0
#
#         for i in range(1, rows):
#             for j in range(1, cols):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0
#
#         if first_row_has_zero:
#             for j in range(cols):
#                 matrix[0][j] = 0
#
#         if first_col_has_zero:
#             for i in range(rows):
#                 matrix[i][0] = 0
