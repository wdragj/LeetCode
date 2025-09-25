class Solution:
    def fib(self, n: int) -> int:
        # DP
        # Time complexity: O(n)
        # Recurrence relation: F(n) = F(n - 1) + F(n - 2), for n > 1.
        dp = [0] * 31
        
        # Base case:
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]