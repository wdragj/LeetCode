class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Visited lists for rows, columns, and 3x3 sub-boxes
        row_vis = [[False for _ in range(10)] for _ in range(10)]
        col_vis = [[False for _ in range(10)] for _ in range(10)]
        box_vis = [[False for _ in range(10)] for _ in range(10)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num != ".": # Skip empty cells
                    digit = int(num)

                    box_idx = (i // 3) * 3 + (j // 3) + 1

                    # Check if exists
                    if row_vis[i][digit] or col_vis[j][digit] or box_vis[box_idx][digit]:
                        return False
                    
                    row_vis[i][digit] = True
                    col_vis[j][digit] = True
                    box_vis[box_idx][digit] = True
        return True