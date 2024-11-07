from collections import deque

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        d = deque(nums)
        
        while d[l] > d[r]:
            d.rotate(1)
        
        return d[0]