class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return True
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m * n) - 1

        while l <= r:
            mid = (l + r) // 2
            col, row = mid % n, (mid // n)

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False