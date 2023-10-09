class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numDict = {}
        for n in nums:
            if n in numDict:
                numDict[n] += 1
            else:
                numDict[n] = 1
        
        for itms in numDict.items():
            k, v = itms
            if v == 1:
                return k