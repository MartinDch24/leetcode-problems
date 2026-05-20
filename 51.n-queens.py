class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()  # Track cols where there already is a queen
        diag1 = set()  # Track both main diagonals
        diag2 = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                # Check for interference with another queen
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res