#Resolved
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = ((0, -1), (0, 1), (-1, 0), (1, 0))

        stack = []
        # Add bordering cells that are "O" to the stack and mark them as safe ("S")
        for i in range(m):
            if i == 0 or i == m-1:
                for j in range(n):
                    if board[i][j] == "O":
                        stack.append([i, j])
                        board[i][j] = "S"
            else:
                for j in [0, n-1]:
                    if board[i][j] == "O":
                        stack.append([i, j])
                        board[i][j] = "S"

        # Do DFS, to find all Os connected to the ones on the borders
        while stack:
            r, c = stack.pop()

            for d1, d2 in directions:
                new_r = r+d1
                new_c = c+d2
                if 0 <= new_r < m and 0 <= new_c < n:
                    if board[new_r][new_c] == "O":
                        stack.append([new_r, new_c])
                        board[new_r][new_c] = "S"
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"