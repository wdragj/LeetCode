class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start from the last day and work backwards
        dp = [0] * len(prices)
        max_sell = prices[-1]

        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > max_sell:
                max_sell = prices[i]
                dp[i] = 0
            else:
                dp[i] = max_sell - prices[i]

        return max(dp)
