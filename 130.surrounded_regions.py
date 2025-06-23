class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        s = []
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for i in range(m):
            for j in [0, n-1]:
                if board[i][j] == "O":
                    board[i][j] ="S"
                    s.append((i, j))
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "S"
                    s.append((i, j))

        while s:
            r, c = s.pop()

            for dr, dc in directions:
                nr = r+dr
                nc = c+dc

                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == "O":
                        board[nr][nc] = "S"
                        s.append((nr, nc))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"