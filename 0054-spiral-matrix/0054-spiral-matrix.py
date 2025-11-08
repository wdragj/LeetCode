class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        spiral_order = []
        while matrix:
            # 1) Add first row
            spiral_order += matrix.pop(0)

            # 2) Add all last elements in order
            if matrix and matrix[0]:
                for row in matrix:
                    spiral_order.append(row.pop())

            # 3) Add reverse of last row
            if matrix:
                spiral_order += matrix.pop()[::-1]

            # 4) Add first element of all row in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    spiral_order.append(row.pop(0))
        
        return spiral_order