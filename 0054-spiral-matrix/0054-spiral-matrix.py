class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        spiral_order = []
        right, down, left, up = n, m, 0, 0

        while True:
            # Scan right
            for r in range(left, right):
                spiral_order.append(matrix[up][r])
            up += 1
            if len(spiral_order) == (n * m):
                break
            # Scan down
            for d in range(up, down):
                spiral_order.append(matrix[d][right - 1])
            right -= 1
            if len(spiral_order) == (n * m):
                break
            # Scan left
            for l in range(right - 1, left - 1, -1):
                spiral_order.append(matrix[down - 1][l])
            down -= 1
            if len(spiral_order) == (n * m):
                break
            # Scan up
            for u in range(down - 1, up - 1, -1):
                spiral_order.append(matrix[u][left])
            left += 1
            if len(spiral_order) == (n * m):
                break

        return spiral_order