class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # There are n kids with candies
        # Given an integer array candies
        # where each candies[i] represents the number of candies the ith kid has
        # And an integer extraCandies, denoting the number of extra candies that you have
        # Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extra candies
        # They will have the greatest number of candies among all the kids, or false otherwise
        
        # 1. True if i + extra >= max
        # 2. False if i + extra < max
        
        # Returned answer
        ans = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies): # 1.
                ans.append(True)
            else: # 2.
                ans.append(False)
        
        return ans