import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        visited.add((0, 0))

        while min_heap:
            level, r, c = heapq.heappop(min_heap)
            if r == N - 1 and c == N - 1:
                return level

            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc

                if next_r < 0 or next_c < 0 or next_r == N or next_c == N or (next_r, next_c) in visited:
                    continue
                visited.add((next_r, next_c))
                heapq.heappush(min_heap, (max(level, grid[next_r][next_c]), next_r, next_c))