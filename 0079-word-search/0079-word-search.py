class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        first_letter = word[0]

        def backtrack(row: int, col: int, k: int) -> bool:
            if board[row][col] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            tmp = board[row][col]
            board[row][col] = None

            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_col = row + d[0], col + d[1]
                if (0 <= next_row < m) and (0 <= next_col < n) and board[next_row][next_col]:
                    if backtrack(next_row, next_col, k + 1):
                        return True
            board[row][col] = tmp
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == first_letter:
                    if backtrack(r, c, 0):
                        return True
        return False