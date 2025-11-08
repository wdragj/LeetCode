from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        island_count = 0
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1
                    queue = deque()
                    queue.append((r, c))
                    visited.add((r, c))
                    while queue:
                        row, col = queue.popleft()

                        for d in dirs:
                            next_row, next_col = row + d[0], col + d[1]
                            if 0 <= next_row < m and 0 <= next_col < n and grid[next_row][next_col] == "1" and (next_row, next_col) not in visited:
                                queue.append((next_row, next_col))
                                visited.add((next_row, next_col))
        return island_count