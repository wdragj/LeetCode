class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP
        dp = [1] * len(nums)

        max_res = 1
        for i in range(1, len(nums)):
            curr_max = 0
            for j in range(i - 1, -1, -1):
                # Recurrence relation:
                # DP[i] is strictly increasing
                if nums[j] < nums[i]:
                    curr_max = max(curr_max, dp[j])
                
            # Update dp array
            dp[i] = curr_max + 1
            max_res = max(max_res, dp[i])
        
        return max_res