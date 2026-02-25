class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, col_set, diag_set, anti_diag_set):
            nonlocal ans
            if row == n:
                ans += 1

            for col in range(n):
                    if col not in col_set and row + col not in diag_set and row - col not in anti_diag_set:
                        col_set.add(col)
                        diag_set.add(row + col)
                        anti_diag_set.add(row - col)
                        backtrack(row + 1, col_set, diag_set, anti_diag_set)
                        col_set.remove(col)
                        diag_set.remove(row + col)
                        anti_diag_set.remove(row - col)
        
        ans = 0
        backtrack(0, set(), set(), set())
        return ans