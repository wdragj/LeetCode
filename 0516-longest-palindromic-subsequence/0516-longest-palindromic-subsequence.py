class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single characters
        for i in range(n):
            dp[i][i] = 1
        
        # Fill for all substring lengths from 2 to n
        for length in range(2, n + 1):  # length of substring
            for i in range(n - length + 1):  # starting index
                j = i + length - 1  # ending index
                
                if s[i] == s[j]:
                    # Characters match - add 2 to inner subsequence
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    # Characters don't match - take max of two options
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]