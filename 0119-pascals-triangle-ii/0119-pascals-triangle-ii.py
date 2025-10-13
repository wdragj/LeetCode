class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Base case:
        # idx-0 = [1]
        # idx-1 = [1, 1]
        dp = [[1] * i for i in range(1, rowIndex+2)]

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp[rowIndex]