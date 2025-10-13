class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base case:
        # 1st row is [1]
        # 2nd row is [1, 1]
        dp = [[1] * i for i in range(numRows+1)]
        dp[1] = [1]

        for i in range(3, numRows+1):
            for j in range(1, i-1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
        return dp[1:numRows+1]