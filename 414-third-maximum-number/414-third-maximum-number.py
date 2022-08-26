class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Given an int array "nums"
        # return the THIRD DISTICT MAXIMUM number in nums
        # if the third maximum doesn't exist, return the maximum number
        
        
        setNums = list(set(nums))
        
        # Using selection sort
        for i in range(len(setNums) - 1):
            maxV = i
            
            for j in range(i + 1, len(setNums)):
                if setNums[j] > setNums[maxV]:
                    maxV = j
            
            if maxV != i: # if min changed, swap
                setNums[i], setNums[maxV] = setNums[maxV], setNums[i]
        
        if len(setNums) < 3:        # if length of setNums is less than 3
            return max(setNums)     # return max
        else:                       
            return setNums[2]       # else return the 2nd index (3rd maximum)