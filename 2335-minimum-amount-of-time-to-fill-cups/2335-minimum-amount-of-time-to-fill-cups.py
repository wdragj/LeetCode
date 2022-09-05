class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Given a 0-indexed int array "amount" of len 3
        # amount[0], amount[1], amount[2] denote number of cold, warm, and hot water cups, respectively
        # COLD, WARM, HOT
        # Return the min number of sec needed to fill up all the cups
        
        res = 0
        amount.sort()
        
        while amount[-2] > 0:
            amount[-1] -= 1
            amount[-2] -= 1
            res += 1
            amount.sort()
        res += amount[-1]
        
        return res