class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        chess_board = ["." * n for _ in range(n)]
        def backtrack(col_set: set, diag_set: set, anti_diag: set, row: int) -> None:
            if row == n:
                ans.append(chess_board[:])
            for col in range(n):
                if (col not in col_set) and (row - col not in diag_set) and (row + col not in anti_diag):
                    col_set.add(col)
                    diag_set.add(row - col)
                    anti_diag.add(row + col)
                    tmp = chess_board[row]
                    chess_board[row] = chess_board[row][:col] + "Q" + chess_board[row][col + 1:]
                    backtrack(col_set, diag_set, anti_diag, row + 1)
                    chess_board[row] = tmp
                    col_set.remove(col)
                    diag_set.remove(row - col)
                    anti_diag.remove(row + col)
        backtrack(set(), set(), set(), 0)
        return ans