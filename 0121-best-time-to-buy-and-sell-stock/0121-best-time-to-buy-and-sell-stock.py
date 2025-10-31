class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        dp[-1] = 0
        max_sell = prices[-1]

        for i in range(n - 2, -1, -1):
            if prices[i] <= max_sell:
                dp[i] = max_sell - prices[i]
            
            # Update max sell
            max_sell = max(prices[i], max_sell)
        
        return max(dp)