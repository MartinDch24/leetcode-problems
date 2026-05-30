#Resolved
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            for d1, d2 in directions:
                new_r = r + d1
                new_c = c + d2

                if 0 <= new_r < m and 0 <= new_c < n:
                    if board[new_r][new_c] == word[i]:
                        if dfs(new_r, new_c, i + 1):
                            board[r][c] = temp
                            return True

                            # Couldn't continue the word from this cell, so we move backwards
            board[r][c] = temp
            return False

        for r in range(m):
            for c in range(n):
                # Try to form the word from all possible start letters
                if board[r][c] == word[0]:
                    if dfs(r, c, 1):
                        return True

        return False