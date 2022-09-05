class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Given a 0-indexed int array "amount" of len 3
        # amount[0], amount[1], amount[2] denote number of cold, warm, and hot water cups, respectively
        # COLD, WARM, HOT
        # Return the min number of sec needed to fill up all the cups
        
        return max(max(amount), (sum(amount) + 1) // 2)