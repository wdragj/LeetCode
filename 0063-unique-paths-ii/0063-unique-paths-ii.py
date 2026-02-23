class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = "*"
        if obstacleGrid[0][0] == "*":
            return 0
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    obstacleGrid[0][0] = 1
                elif obstacleGrid[r][c] == "*":
                    continue
                else:
                    up = obstacleGrid[r-1][c] if 0 <= r-1 < m and obstacleGrid[r-1][c] != "*" else 0
                    left = obstacleGrid[r][c-1] if 0 <= c < n and obstacleGrid[r][c-1] != "*" else 0
                    obstacleGrid[r][c] = up + left
        return obstacleGrid[m-1][n-1] if obstacleGrid[m-1][n-1] != "*" else 0