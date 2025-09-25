class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        # Recurrence relation: max(DP[i-1], DP[i-2] + L[i])
        n = len(nums)
        dp = [0] * n
        # Base case:
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return max(dp)