import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            k = (l + r) // 2

            calcH = 0
            
            # Eat piles
            for b in piles:
                calcH += math.ceil(b/k)
            
            # If less than h, search left
            if calcH <= h:
                ans = min(ans, k)
                r = k - 1
            # If greater than h, search right
            elif calcH > h:
                l = k + 1
        
        return ans