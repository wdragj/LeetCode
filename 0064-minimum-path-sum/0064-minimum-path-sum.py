import heapq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1)]
        pq = [(grid[0][0], (0, 0))]
        visited = set()
        visited.add((0, 0))
        while pq:
            distance, (r, c) = heapq.heappop(pq)
            if r == m - 1 and c == n - 1:
                return distance
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(pq, (distance + grid[nr][nc], (nr, nc)))
        return 0