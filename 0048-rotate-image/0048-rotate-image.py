class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        map = {}
        n = len(matrix)

        tmp = n - 1
        for r in range(n):
            for c in range(n):
                map[(c, tmp)] = matrix[r][c]
            tmp -= 1
        
        for r in range(n):
            for c in range(n):
                matrix[r][c] = map[(r, c)]