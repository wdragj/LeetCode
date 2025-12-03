class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Edge cases
        if not nums:
            return nums
        
        if nums[0] >= 0:
            return [num**2 for num in nums]
        
        # Find the first index that is positive
        idx = 0
        for i, v in enumerate(nums):
            if v >= 0:
                idx = i
                break
        
        # All negative
        if idx == 0:
            return [n**2 for n in reversed(nums)]
        
        # Split into two partitions
        A = nums[idx:len(nums)] # Positive section
        B = [-1*n for n in reversed(nums[:idx])] # Negative section

        a, b = 0, 0 # Two pointers for splitted partition
        res = []
        while a < len(A) and b < len(B):
            # a is smaller
            if A[a] < B[b]:
                res.append(A[a])
                a += 1
            # b is smaller
            else:
                res.append(B[b])
                b += 1
            
        if a < len(A):
            res.extend(A[a:])
        else:
            res.extend(B[b:])
        
        return [n**2 for n in res]