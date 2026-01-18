class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        q = deque([])
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O" and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                    q.append((r, c))
        while q:
            row, col = q.popleft()
            board[row][col] = "*"
            for d in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                next_r, next_c = row + d[0], col + d[1]
                if (0 <= next_r < m and 0 <= next_c < n) and board[next_r][next_c] == "O":
                    q.append((next_r, next_c))


        # def dfs(r: int, col: int) -> None:
        #     board[r][c] = "*"
        #     for d in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        #         next_r, next_c = r + d[0], c + d[1]
        #         if (0 <= next_r < m and 0 <= next_c < n) and board[next_r][next_c] == "O":
        #             dfs(next_r, next_c)

        # for r in range(m):
        #     for c in range(n):
        #         if board[r][c] == "O" and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
        #             dfs(r, c)
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == "*":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"