from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0
        visited = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))
                    area = 0
                    while q:
                        r, c = q.popleft()
                        area += 1
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                                q.append((nr, nc))
                                visited.add((nr, nc))
                    max_area = max(max_area, area)
        return max_area
