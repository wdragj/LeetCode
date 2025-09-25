class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # DP
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # Base case: Only one number - take it
        for i in range(n):
            dp[i][i] = nums[i]
        
        # Subarray length 2 to n 
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Taking left: V(i + 1, j) remains
                # V_i + min(V(i + 2, j), V(i + 1, j - 1))
                take_left = nums[i] + min(
                    dp[i + 2][j] if i + 2 <= j else 0,          # Opp takes left:  V(i + 2, j)
                    dp[i + 1][j - 1] if i + 1 <= j - 1 else 0   # Opp takes right: V(i + 1, j - 1)
                )

                # Taking right: V(i, j - 1) remains
                # V_j + min(V(i + 1, j - 1), V(i, j - 2))
                take_right = nums[j] + min(
                    dp[i + 1][j - 1] if i + 1 <= j + 1 else 0,  # Opp takes left:  V(i + 1, j - 1)
                    dp[i][j - 2] if i <= j - 2 else 0           # Opp takes right: V(i, j - 2)
                )

                # Taking max of two
                dp[i][j] = max(take_left, take_right)
        
        total_sum = sum(nums)
        max_player1 = dp[0][n-1]

        return max_player1 >= (total_sum + 1)//2