class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1: # Base case
            return [["Q"]]
        
        col = set()
        neg_diag = set() # (R - C)
        pos_diag = set() # (R + C)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r - c) in neg_diag or (r + c) in pos_diag:
                    continue
                
                col.add(c)
                neg_diag.add(r - c)
                pos_diag.add(r + c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                col.remove(c)
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                board[r][c] = "."
        
        backtrack(0)
        return res